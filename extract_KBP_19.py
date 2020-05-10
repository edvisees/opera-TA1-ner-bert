import sys
import os
from document import read_ltf_offset
import numpy as np
annotation_file = sys.argv[1]
annotation = {}
src_folder_path = sys.argv[2]
file_list = []
with open(annotation_file) as f:
	next(f)
	for line in f:
		line = line.strip().split('\t')
		key = line[1]
		file, offset = line[3].split(':')
		text = line[2]
		offset = list(map(int, offset.split('-')))
		men_type = line[5]
		if file not in annotation:
			annotation[file] = []
		annotation[file].append([key, text, offset, men_type])
		file_list.append(file)

file_list = list(set(file_list))
with open('dev.txt', 'w') as devf, open('train.txt', 'w') as trainf, open('type_train.txt', 'w') as type_trainf, open('type_dev.txt', 'w') as type_devf:
	for file in file_list:
		sents_label = []
		sents, doc = read_ltf_offset(os.path.join(src_folder_path, file + '.ltf.xml'))
		sent_cut_id = [0]
		word_list = []
		sents_label = []
		for sent in sents:
			sents_label.extend(['O'] * len(sent.words))
			sent_cut_id.append(len(sents_label))
			word_list.extend(sent.words)
		assert len(word_list) == len(sents_label)

		for ann in annotation[file]:
			key, text, offset, men_type = ann
			print(text, offset, file)
			men_type = men_type.split('.')
			men_type[0] = men_type[0].upper()
			for i in range(1, len(men_type)):
				men_type[i] = men_type[i].lower().capitalize() 
			men_type = '.'.join(men_type)
			word_len = len(text.split(' '))
			for i in range(len(word_list) - word_len):
				if ' '.join([word.word for word in word_list[i:i+word_len]]) == text:
					if word_list[i].begin == offset[0]:
						flag = True
						for j in range(word_len):
							if j == 0:
								if sents_label[i+j] != 'B-'+men_type:
									flag = False
									break
							else:
								if sents_label[i+j] != 'I-'+men_type:
									flag = False
									break
						for j in range(word_len):
							assert sents_label[i+j] == 'O' or flag
							if j == 0:
								sents_label[i+j] = 'B-' + men_type
							else:
								sents_label[i+j] = 'I-' + men_type
						break
		prob = np.random.uniform()
		if prob < 0.1:
			f = devf
		else:
			f = trainf
		for idx, (word, label) in enumerate(zip(word_list, sents_label)):
			if idx in sent_cut_id:
				f.write('\n')
			f.write(' '.join((str(idx), word.word, '--', '--', label)) + '\n')
		f.write('\n')
		if prob < 0.1:
			f = type_devf
		else:
			f = type_trainf
		for idx, (word, label) in enumerate(zip(word_list, sents_label)):
			label = label.split('.')[0]
			if idx in sent_cut_id:
				f.write('\n')
			f.write(' '.join((str(idx), word.word, '--', '--', label)) + '\n')
		f.write('\n')
	