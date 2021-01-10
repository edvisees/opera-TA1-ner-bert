import sys
file = sys.argv[1]
count = 0
entity_type_dict = {}
with open(file) as f:
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
