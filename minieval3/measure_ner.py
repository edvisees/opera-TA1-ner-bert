import os
import json
label_folder = 'label_folder/data/'
out_folder = 'minieval-3-ner-out'
eval_file_list = []
for file in os.listdir(out_folder):
	eval_file_list.append(file.split('.')[0])
print(eval_file_list)
labels = {}
for topic in ['E101', 'E102', 'E103']:
	for file in os.listdir(label_folder + topic):
		if 'arg' not in file:
			continue
		file_path = os.path.join(label_folder, topic, file)
		with open(file_path) as f:
			next(f)
			for line in f:
				line = line.strip().split('\t')
				file_name = line[2]
				if file_name in eval_file_list:
					if file_name not in labels:
						labels[file_name] = []
					labels[file_name].append([line[3], line[4], line[5], line[12:15]])
total = 0.
type_correct = 0.
subtype_correct = 0.
ssubtype_correct = 0.
total_pred = 0.
for file in eval_file_list:
	with open(os.path.join(out_folder, file + '.ltf.xml.json')) as f:
		label_json = json.load(f)
		for label in label_json:
			for fm in label['fillerMentions'] + label['nominalMentions'] + label['namedMentions']:
				total_pred += 1

best_candi = None
for file in eval_file_list:
	with open(os.path.join(out_folder, file + '.ltf.xml.json')) as f:
		label_json = json.load(f)
		for gold in labels[file]:
			total += 1
			gold_type = 'ldcont:'+'.'.join(gold[3]).lower()
			gold_type = gold_type.replace('.unspecified', '')
			gold_type_split = gold_type.split('.')
			gtype = gold_type_split[0]
			gsubtype = '' if len(gold_type_split) < 2 else gold_type_split[1]
			gssubtype = '' if len(gold_type_split) < 3 else gold_type_split[2]
			start, end = list(map(int, gold[:2]))
			max_correct = 0
			max_correct_list = [0.] * 3
			for label in label_json:
				total_pred += 1
				for fm in label['fillerMentions'] + label['nominalMentions'] + label['namedMentions']:
					fstart, fend = fm['char_begin'], fm['char_end']
					if fstart <= start and fend >= end:
						correct = 0
						cur_correct_list = [0.] * 3
						ptype_split = fm['type'].lower().split('.')
						ptype = ptype_split[0]
						psubtype = '' if len(ptype_split) < 2 else ptype_split[1]
						pssubtype = '' if len(ptype_split) < 3 else ptype_split[2]
						# print(psubtype, gsubtype)
						# if ptype != gtype:
						# 	print(file, ptype, gtype, gold[2])
						if ptype == gtype:
							correct += 1
							cur_correct_list[0] = 1
							if psubtype == gsubtype:
								correct += 1
								cur_correct_list[1] = 1
								if pssubtype == gssubtype:
									correct += 1
									cur_correct_list[2] = 1
						if correct > max_correct:
							max_correct = correct
							max_correct_list = cur_correct_list
							best_candi = [ptype, psubtype, pssubtype]

			if best_candi and best_candi[0] == gtype and best_candi[1] != gsubtype:
				print(file, best_candi[1], gsubtype, gssubtype,gold[2], gold[0])
			# print(max_correct)
			type_correct += max_correct_list[0]
			subtype_correct += max_correct_list[1]
			ssubtype_correct += max_correct_list[2]

print(total, type_correct, subtype_correct, ssubtype_correct)





				
