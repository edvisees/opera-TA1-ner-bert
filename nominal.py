from stanfordcorenlp import StanfordCoreNLP
from tree import *
from collections import deque
from dictionary import stopwords, other_pronouns
from wordnet import get_semantic_class, get_semantic_class_with_subtype
from functools import cmp_to_key
from zs_mapper import A20_NER_MAP
nist_key = {}
for k, vs in A20_NER_MAP.items():
    for v in vs:
        nist_key[v] = 'ldcOnt:' + k 
nist_key['people'] = 'ldcOnt:PER'
entity_type_dict = {}
with open('type_entity.tab') as f:
    for line in f:
        entity_type, entity = line.strip().split('\t')
        if 'a.k.a.' in entity:
            entities = entity.split(' ')
            refined_entites = []
            for en in entities[:-1]:
                if 'a.k.a' in en:
                    entity_type_dict[en] = entity_type
            if entities[-1].endswith(')'):
                entity_type_dict[entities[-1][:-1]] = entity_type
            else:
                entity_type_dict[entities[-1]] = entity_type
        else:
            entity_type_dict[entity] = entity_type

def read_gazetteer_list(file_path):
    gaze_list = set()
    with open(file_path, 'r') as f:
        for line in f:
            gaze_list.add(line.strip().lower())
    return gaze_list
mhi_list = read_gazetteer_list('gazetteer/mhi.lst')
vaccine_list = read_gazetteer_list('gazetteer/vaccine.lst')
virus_list = read_gazetteer_list('gazetteer/vaccine.lst')
# with open('gazetteer/vaccine.lst')
# with open('gazetteer/mhi.lst', 'r') as f:
#     mhi_kb_dic = {}
#     for line in f:
#         mhi_list.add(line.strip().lower())

def extract_nominals(sent, nlp, ners):
    mentions = extract_NP_or_PRP(sent, nlp)
    mentions = remove_spurious_mentions(mentions, ners)
    mentions = remove_duplicate_mentions(mentions)
    for m in mentions:
        m['type'], m['subtype'], m['subsubtype'] = get_semantic_class_with_subtype(m['headword'])
        
        for k, v in nist_key.items():    
            if k in m['mention'].lower().split():
                m['type'], m['subtype'], m['subsubtype'] = v, v, v
                break
        if  any(s in m['headword'].lower() for s in ['cases', 'fatalities', 'vote']):
            m['type'], m['subtype'], m['subsubtype'] = 'ldcOnt:PER', 'PER', 'PER'
        elif any(s in m['headword'].lower() for s in ['system', 'institute']):
            m['type'], m['subtype'], m['subsubtype'] = 'ldcOnt:ORG', 'ORG', 'ORG'
        elif 'fund' in  m['headword'].lower():
            m['type'], m['subtype'], m['subsubtype'] = 'ldcOnt:MON', 'MON', 'MON'
        # elif 'medicine' in  m['headword'].lower() or 'sample' in m['headword'].lower():
        #     m['type'], m['subtype'], m['subsubtype'] = 'ldcOnt:COM', 'MON', 'MON'
        # elif 'caribbean' in  m['headword'].lower():
        #     m['type'], m['subtype'], m['subsubtype'] = 'ldcOnt:LOC.Position.Region', 'LOC', 'LOC'
        elif 'drone' in m['headword'].lower():
            m['type'], m['subtype'], m['subsubtype'] = 'ldcOnt:VEH.Aircraft.Drone', 'Aircraft', 'Drone'
        elif any(s in m['headword'].lower() for s in ['covid', 'coronovirus']):
            m['type'], m['subtype'], m['subsubtype'] = 'PTH.virus.coronovirus', 'PTH', 'virus'
        elif m['headword'].lower() in mhi_list:
            m['type'], m['subtype'], m['subsubtype'] = 'ldcOnt:MHI.Disease.Disease', 'MHI', 'Disease'
        elif m['headword'].lower() in vaccine_list:
            m['type'], m['subtype'], m['subsubtype'] = 'ldcOnt:COM.vaccine', 'COM', 'vaccine'
    mentions = list(filter_nominals(mentions))
    return mentions

def extract_NP_or_PRP(sent, nlp):
    raw_tree = nlp['parse']
    if raw_tree is None:
        return []
    tree = Tree.parse_tree(raw_tree)
    if len(sent.words) != tree.get_span()[1]:
        # TODO
        return []

    NPs = []
    stack = deque()
    stack.append(tree)
    while len(stack) > 0:
        tree = stack.pop()
        if tree.tag == 'NP':
            word_span = tree.get_span()
            text = sent.sub_string(*word_span)
            begin_offset = sent.words[word_span[0]].begin
            end_offset = sent.words[word_span[1]-1].end
            head_index = find_head_of_np(tree)
            headword = sent.words[head_index].word
            NPs.append({'token_span': word_span, 'word_span': word_span, 'mention': text, 'char_begin': begin_offset-1, 'char_end': end_offset, 'head_index': head_index, 'head_span': [sent.words[head_index].begin-1, sent.words[head_index].end], 'headword': headword, 'category': 'NOM', 'score': 0.9})
        if tree.children:
            for child in reversed(tree.children):
                stack.append(child)

    return NPs

def set_bare_plural():
    pass

non_words = set(["mm", "hmm", "ahem", "um", "uh", "%mm", "%hmm", "%ahem", "%um", "%uh"])
quantifiers = set(["not", "every", "any", "none", "everything", "anything", "nothing", "all", "enough"])
bare_NP_words = set(["sense", "case", "now", "here", "there", "who", "whom", "whose", "where", "when", "which"])

def remove_spurious_mentions(mentions, ners):
    filtered = []
    for m in mentions:
        headword = m['headword'].lower()
        if headword in non_words:
            continue
        if m['word_span'][1] - m['word_span'][0] == 1:
            if headword in quantifiers:
                continue
            if headword in bare_NP_words:
                continue
            if headword in stopwords:
                continue
            if headword in other_pronouns:
                continue
        if headword == "%":
            continue
        #if ners and ners[m['head_index']] != 'O':
            #continue
         
        filtered.append(m)
    return filtered
        
def remove_duplicate_mentions(mentions):
    #print(mentions)
    to_remove = set()
    mentions = sorted(mentions, key=cmp_to_key(lambda a, b: 
        ((a['word_span'][1] - a['word_span'][0] - b['word_span'][1] - b['word_span'][0])) if a['head_index'] == b['head_index'] else a['head_index'] - b['head_index']))
    for i in range(len(mentions)):
        mention1 = mentions[i]
        for j in range(i+1, len(mentions)):
            mention2 = mentions[j]
            if mention1['head_index'] == mention2['head_index']:
                to_remove.add(j)
    return [mention for (wid, mention) in enumerate(mentions) if wid not in to_remove]

def load_ontology_vocab():
    ontology = set()
    with open('ontology/ontology_entity.txt', 'r') as f:
        for line in f:
            ontology.add(line.strip())
    return ontology

ontology = load_ontology_vocab()

def filter_nominals(mentions):
    return filter(lambda x: x['type'] != 'n/a' or x['subtype'] != 'n/a' or x['subsubtype'] != 'n/a'  , mentions) #and x['headword'] in ontology
