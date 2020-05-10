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
		if 'rel_mentions' not in file:
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
total = 0
for file in eval_file_list:
	with open(os.path.join(out_folder, file + '.ltf.xml.json')) as f:
		label_json = json.load(f)
		for gold in labels.get(file, []):
			total += 1
print(total)