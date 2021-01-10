import sys
import json
import os
pred_folder = sys.argv[1]
ann_folder = sys.argv[2]
pred_dict = {}

def process_ann_file(ann_file_path):
	ann_dict = {}
	with open(ann_file_path) as f:
		next(f)
		for line in f:
			line = line.strip().split('\t')
			file_name = line[2]
			if file_name not in ann_dict:
				ann_dict[file_name] = []
			token_mention = line[5]
			token_span = line[3:5]
			en_type = line[12:15]
			ann_dict[file_name].append((token_mention, token_span, en_type))
	return ann_dict
for file in os.listdir(pred_folder):
	if not file.endswith('.json'):
		continue
	with open(os.path.join(pred_folder, file)) as f:
		cur_pred = json.load(f)
	pred_dict[file] = cur_pred
ann_dict = {}
for root, dirs, files in os.walk(ann_folder):
	for file in files:
		if 'arg_mentions.tab' in file:
			abs_file = os.path.join(root, file)
			ann_dict.update(process_ann_file(abs_file))
total = 0
type_correct = 0
stype_correct = 0
sstype_correct = 0
for key, item in pred_dict.items():
	name = key.split('.')[0]
	if name in ann_dict:
		ann_list = ann_dict[name]
		for ann_item in ann_list:
			total += 1
			type_is_correct = False
			stype_is_correct = False
			for pred_all in item:
				if pred_all['offset'] <= int(ann_item[1][1]):
					pred_items = pred_all['namedMentions'] + pred_all['nominalMentions'] + pred_all['fillerMentions']
					for pred_item in pred_items:
						overlap = max(0, min(pred_item['char_end'], int(ann_item[1][1])) - max(pred_item['char_begin'], int(ann_item[1][0])))
						# if pred_item['char_begin'] >= int(ann_item[1][0]) and pred_item['char_end'] - 1 <= int(ann_item[1][1]):
						if overlap > 0:
							pred_type = pred_item['type'].split(':')[1].split('.')
							if len(pred_type) == 1:
								pred_type.extend(['unspecified', 'unspecified'])
							elif len(pred_type) == 2:
								pred_type.extend(['unspecified'])

							if pred_type[0].lower() == ann_item[2][0].lower():
								type_correct += 1
								type_is_correct = True
							else:
								continue
							if pred_type[1].lower() == ann_item[2][1].lower():
								stype_correct += 1
								stype_is_correct = True
							if pred_type[2].lower() == ann_item[2][2].lower():
								sstype_correct += 1
							break
				if type_is_correct:
					break
			if not stype_is_correct:
				print(ann_item, name)

							
print(total, type_correct, stype_correct, sstype_correct)

				



