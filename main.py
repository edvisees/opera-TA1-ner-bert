from stanfordcorenlp import StanfordCoreNLP
from document import *
from ner import *
from nominal import *
from filler import *
from typing import *
import json
import pickle
import sys
from collections import defaultdict
from multiprocessing.dummy import Pool as ThreadPool
import time
from threading import Semaphore
import json
import traceback
from zs_mapper import A20_NER_MAP
script_dir=os.path.dirname(os.path.realpath(__file__))
with open('gazetteer/ldc2wikidata.txt', 'r') as f:
    ldc2wd_dict = {}
    for line in f:
        line = line.strip().split('\t')
        if len(line) > 2:
            ldc2wd_dict[line[1].lower()] = line[2]
with open('covid_ontology.json', 'r') as f:
    covid_ontology = json.load(f)

covid_ent_ontology = defaultdict(list)
for k, v in covid_ontology['entities'].items():
    assert len(v) == 1
    wd_node = v[0]['wd_node']
    ldc_types = v[0]['ldc_types']
    for ldc_type in ldc_types:
        covid_ent_ontology[ldc_type['name'].replace('.Unspecified', '').lower()].append(wd_node)

nist_ner = []
aida_ner_type = {}
with open('aida_ner.txt') as f:
    next(f)
    for line in f:
        line = line.strip().split()
        if line[3] == 'n/a' or line[3] == 'Unspecified':
            type_name = line[1]
        elif line[5] == 'n/a' or line[5] == 'Unspecified':
            type_name = '.'.join((line[1], line[3]))
        else:
            type_name = '.'.join((line[1], line[3], line[5]))
        type_name = 'ldcOnt:' + type_name
        aida_ner_type[type_name.lower()] = type_name
        nist_ner.append(type_name)

for new_type in ['BOD.fluids', 'BOD.organ', 'COM.Equipment.PPE', 'COM.vaccine', 'PTH.virus', 'PTH.virus.coronovirus']:
    type_name = 'ldcOnt:' + new_type
    nist_ner.append(type_name)
    aida_ner_type[type_name.lower()] = type_name

nist_key = {}
nist_key['people'] = 'ldcOnt:PER'
stype_list = []
sstype_list = []
for nn in nist_ner:
    ori_nn = nn
    nn = nn.split(':')[1]
    nn = nn.split('.')
    if len(nn) == 1:
        n_type = nn[0]
    elif len(nn) == 2:
        n_type, n_stype = nn
        if n_stype not in stype_list:
            stype_list.append(n_stype)
            if n_stype.lower() in ['police', 'politician', 'protester', 'aircraft', 'militaryvehicle', 'rocket', 
            'watercraft', 'bomb', 'bullets', 'missilesystem']:
                nist_key[n_stype.lower()] = ori_nn
    elif len(nn) == 3:
        n_type, n_stype, n_sstype = nn
        if n_stype not in stype_list:
            stype_list.append(n_stype)
        if n_sstype not in sstype_list:
            sstype_list.append(n_sstype)
            nist_key[n_sstype.lower()] = ori_nn
    else:
        print(nn, 'not correct format')
for k, vs in A20_NER_MAP.items():
    for v in vs:
        if v in nist_key:
            continue
        nist_key[v] = 'ldcOnt:' + k 

nist_key['force'] = 'ldcOnt:PER.MilitaryPersonnel'
nist_key['forces'] = 'ldcOnt:PER.MilitaryPersonnel'
nist_key['soldiers'] = 'ldcOnt:PER.MilitaryPersonnel'
#LOCK = Semaphore(1)


def level_num(inp):
    return len(inp.split('.'))

def run_document(fname, nlp, ontology, decisionsi, out_fname=None, raw=False):
    #raw = True
    print('processing {}'.format(fname))
    try:
        if raw:
            sents, doc = read_raw_text(fname, nlp=nlp)
        else:
            sents, doc = read_ltf_offset(fname, nlp=nlp)
        if sents is None or doc is None:

            print('ner skipped {}'.format(fname))
            return
    except Exception as e:
        print('error: {}; skipped {}'.format(str(e), fname))
        return True

    #LOCK.acquire()
    out_doc = []
    for sid, sent in enumerate(sents):
        try:
            named_ents, ners, feats = extract_ner(sent)
            nominals = extract_nominals(sent, sent.annotation, ners)
            nom_list = []
            ner_list = []
            for i in range(len(nominals)):
                
                nom_mention = nominals[i]['mention']
                nom_char_begin = nominals[i]['char_begin']
                for j in range(len(named_ents)):
                    ner_mention = named_ents[j]['mention']
                    ner_char_begin = named_ents[j]['char_begin']
                    if nom_mention == ner_mention and ner_char_begin == nom_char_begin:
                        named_ents[j]['type'] = nominals[i]['type']
                        # if level_num(nominals[i]['type']) >= level_num(nominals[i]['type']):
                        # # if 'n/a' in nominals[i]['subtype']:
                        nom_list.append(i)
            # named_ents = [i for j, i in enumerate(named_ents) if j not in ner_list]
            nominals = [i for j, i in enumerate(nominals) if j not in nom_list]
            fillers = extract_filler(sent, sent.annotation, ners)
            fil_list = []
            fillers = sorted(fillers, key=lambda tupe: int(tupe['char_begin']))
            f_i = 0
            f_j = 1
            for m_id, mention in enumerate(fillers):
                ner_type = mention['type'].lower()
                mention['@id'] = 'LDC2018E01-opera-text-entity-mention-{}-s{}-e{}'.format(os.path.split(fname)[1], sid,  m_id)             
                contain = False
                if ner_type == 'NUMERICAL'.lower():
                    ner_type = 'VAL.Number.Number'
                if ner_type == 'URL'.lower():
                    ner_type = 'VAL'
                elif ner_type == 'title':
                    ner_type = 'TTL'
                if 'date_time' not in ner_type and ':' not in ner_type:
                    mention['type'] = 'ldcOnt:' + ner_type.upper()
                    
            for m_id, mention in enumerate(named_ents + nominals):
                mention['@id'] = 'LDC2018E01-opera-text-entity-mention-{}-s{}-e{}'.format(os.path.split(fname)[1], sid,  m_id + len(fillers))
                #mention['type'] = normalize_type(mention['type'])
                if mention['type'].startswith('ldc'):
                    continue
                ner_type = mention['type'].lower()
                if 'subtype' not in mention.keys():
                    ner_subtype = '.n/a'
                else:
                    ner_subtype = '.' + mention['subtype'].lower()

                if 'subsubtype' not in mention.keys():
                    ner_subsubtype = '.n/a'
                else:
                    ner_subsubtype = '.' + mention['subsubtype'].lower()
                contain = False
                unknown = 'n/a'

                for n_ner in nist_ner:
                    low_n_ner = n_ner.lower()
                    if unknown not in ner_subsubtype:
                        if ner_subsubtype in low_n_ner:
                            mention['type'] = n_ner
                            contain = True
                            break
                    elif ner_type in low_n_ner and ner_subtype in low_n_ner:
                        mention['type'] = n_ner
                        contain = True
                        break
                    elif ner_type == 'n/a':
                        if ner_subtype in low_n_ner:
                            mention['type'] = n_ner
                            contain = True
                            break
                    elif ner_subtype == '.n/a' or ner_subtype == '.na':
                        if ner_type == 'NUMERICAL'.lower() or ner_type == 'URL'.lower() or ner_type == 'TIME'.lower():
                            ner_type = 'VAL'
                        elif ner_type == 'title':
                            ner_type = 'TTL'
                        mention['type'] = 'ldcOnt:' + ner_type.upper()
                        contain = True
                        break
                if not contain:
                    print(mention, ner_type, ner_subtype, '2')
                    
                single_mention = mention['headword'].lower()
                has = 0
                for sm in single_mention.split(' '):
                    if sm in nist_key:
                        has += 1
                        new_type = nist_key[sm]
                if has == 1:
                    mention['type'] = new_type
                
            def filter_type(nn):
                new_named_ents = []

                for ne in nn:
                    if ne['type'] == 'aida:date_time':
                        new_named_ents.append(ne)
                    elif ne['type'].lower() in aida_ner_type:
                        ne['type'] = aida_ner_type[ne['type'].lower()]
                        new_named_ents.append(ne)
                    else:
                        print(ne['type'], '3')
                nn = new_named_ents
                if len(nn) == 0:
                    return nn
                new_named_ents = []
                entities = sorted(nn, key=lambda tupe: int(tupe['char_end']))
                new_named_ents.append(entities[0])
                for i in range(1, len(entities)):
                    if entities[i]['char_begin'] == new_named_ents[-1]['char_begin'] \
                        and entities[i]['char_end'] == new_named_ents[-1]['char_end']:
                        prev_en = new_named_ents[-1]['type'].split()
                        cur_en = new_named_ents[-1]['type'].split()
                        if len(prev_en) < len(cur_en):
                            new_named_ents[-1] = entities[i]
                        elif len(prev_en) == len(cur_en):
                            if float(entities[i]['score']) > float(entities[-1]['score']):
                                new_named_ents[-1] = entities[i]

                    else:
                        new_named_ents.append(entities[i])
                for idx in range(len(new_named_ents)):
                    inp_type = new_named_ents[idx]['type'][7:]
                    new_named_ents[idx]['wikidata'] = ldc2wd_dict.get(inp_type.lower(), 'none')
                for idx in range(len(new_named_ents)):
                    inp_type = new_named_ents[idx]['type'][7:]
                    wd_node = covid_ent_ontology.get(inp_type.lower(), ['none'])
                    new_named_ents[idx]['wd_node'] = ','.join(wd_node)
                return new_named_ents
            named_ents = filter_type(named_ents)
            nominals = filter_type(nominals)
            fillers =filter_type(fillers)

            new_named_ents = []
            for i in range(len(named_ents)):
                overlapped = False
                for j in range(len(nominals)):
                    cur_entity = named_ents[i]
                    cur_nominal = nominals[j]
                    if max(cur_entity['char_begin'], cur_nominal['char_begin']) <= min(cur_entity['char_end'], cur_nominal['char_end']):
                        if cur_entity['headword'] == cur_nominal['headword']:
                            overlapped = True
                if not overlapped:
                    new_named_ents.append(named_ents[i])
            named_ents = new_named_ents


            out_doc.append({'docID': os.path.split(fname)[1], 'sent_rel': sent.get_text(), 'inputSentence': sent.get_original_string(), 'offset': sent.begin-1, 'namedMentions': named_ents, 'nominalMentions': nominals, 'fillerMentions': fillers})
        except Exception:
            sys.stderr.write("ERROR: Exception occurred while processing {0}, sentence: {1}\n".format(fname, sent.get_original_string()))
            traceback.print_exc()
    if not out_fname:
        out_fname = fname + '.json'
    with open(out_fname, 'w', encoding='utf8') as f:
        json.dump(out_doc, f, indent=1, sort_keys=True, ensure_ascii=False)

    print('processed {}'.format(fname))
    #LOCK.release()
    return True


def normalize_type(t):
    if t == 'GPE':
        return 'GeopoliticalEntity'
    if t == 'ORG':
        return 'Organization'
    if t == 'LOC':
        return 'Location'
    if t == 'PER':
        return 'Person'
    if t == 'FAC':
        return 'Facility'
    if t == 'WEA':
        return 'Weapon'
    if t == 'VEH':
        return 'Vehicle'
    if t == 'URL':
        return 'URL'
    if t == 'TITLE':
        return 'Title'
    if t == 'TIME':
        return 'Time'
    if t == 'NUMERICAL':
        return 'NumericalValue'
    return t

def create_nlp_pool(num_threads):
    return [StanfordCoreNLP('http://localhost', port=9000) for _ in range(num_threads)]



def main():
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    read_raw = False
    if len(sys.argv) > 3:
        read_raw = bool(sys.argv[3])
    print('Reading from {}; writing to {}'.format(input_dir, output_dir))
    #ontology = OntologyType()
    #decisions = ontology.load_decision_tree()
    decisions = None
    # with StanfordCoreNLP('/home/xianyang/stanford-corenlp-full-2017-06-09/') as nlp:
    # with StanfordCoreNLP('http://localhost', port=9006) as nlp:
    with StanfordCoreNLP(os.path.join(script_dir, 'stanford-corenlp-full-2017-06-09'), memory='8g') as nlp:
        start_time = time.time()
        if read_raw:
            files = os.listdir(input_dir)
        else:
            files = filter(lambda x: x.endswith('.xml'), os.listdir(input_dir))
        for file in files:
            try:
                success = run_document(os.path.join(input_dir, file), nlp, ontology, decisions, out_fname=os.path.join(output_dir, file + '.json'))
            except Exception:
                sys.stderr.write("ERROR: Exception occurred while processing {0}\n".format(file))
                traceback.print_exc()
        #pool = ThreadPool(processes=6)
        #success = pool.map(lambda file: run_document(os.path.join(input_dir, file), nlp, ontology, decisions, out_fname=os.path.join(output_dir, file + '.json'), raw=read_raw), files)
        #pool.close()
        #pool.join()
        end_time = time.time()
        print('total elapsed time: {}'.format(end_time - start_time))


if __name__ == '__main__':
    main()