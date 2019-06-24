from functools import reduce

russian_names = set()
with open('gazetteer/russian_names.lst', 'r') as f:
    for line in f:
        line = line.strip().lower()
        russian_names.add(line)
        word = line.split()
        for _, w in enumerate(word):
            if _ == 2:
                break
            russian_names.add(w)

weapon_names = set(['buk', 'buk-telar', '9M38', 'missile'])

organization_names = set()
with open('gazetteer/org.txt') as f:
    for line in f:
        name = line.strip().lower()
        organization_names.add(name)

location_names = set(['euromaidan'])

vehicle_names = set()

country_names = set(['russia', 'ukraine', 'malaysia', 'dutch', 'netherland'])

russian_geonames = set([])
with open('gazetteer/ru.txt', 'r') as f:
    for line in f:
        name = line.strip().lower()
        russian_geonames.add(name)

ukrainian_geonames = set()
with open('gazetteer/ua.txt', 'r') as f:
    for line in f:
        name = line.strip().lower()
        ukrainian_geonames.add(name)

geo_names = russian_geonames.union(ukrainian_geonames)
#print(organization_names)
#exit()
def look_gazetteer(mention, type):
    mention = mention.strip().lower()
    tokens = mention.split()
    possible_type = []
    if reduce(lambda a, b: a and b, [token in russian_names for token in tokens]):
        possible_type.append('PER')
    if mention in weapon_names:
        possible_type.append('WEA')
    if mention in country_names:
        return 'GPE'
    if mention in geo_names:
        possible_type.append('LOC')
        possible_type.append('GPE')
    if mention in organization_names:
        possible_type.append('ORG')
    if mention in location_names:
        possible_type.append('LOC')
    if type in possible_type:
        return None
    if len(possible_type) == 1:
        return possible_type[0]
    else:
        return None

def lookup_gazetteer(mention, type):
    mention = mention.strip().lower()
    tokens = mention.split()
    

    # bigrams = [ '{} {}'.format(tokens[i], tokens[i+1]) for i in range(len(tokens)-1) ] 
    if type != 'PER':
        if reduce(lambda a, b: a and b, [token in russian_names for token in tokens]):
            if mention in organization_names:
                return None
            else:
                return 'PER'

    if mention in weapon_names:
        return 'WEA'

    if type == 'VEH':
        for token in tokens:
            if token in weapon_names:
                return 'WEA'
            if token in geo_names:
                return 'LOC'
            
    if mention in country_names:
        if type != 'GPE' and type != 'LOC':
            return 'GPE'

    if mention in geo_names and mention not in russian_names:
        if type != 'GPE' and type != 'LOC':
            return 'LOC'

    if type != 'ORG':
        if mention in organization_names:
            return 'ORG'

    if type != 'LOC':
        if mention in location_names:
            return 'LOC'

    return None


if __name__ == '__main__':
    names = []
    with open('../../geonames/UA/UA.txt') as f:
        for line in f:
            split = line.strip().split('\t')
            name = split[1]
            aliases = split[3].split(',')
            names.append(name)
            for alias in aliases:
                if len(alias) > 0:
                    names.append(alias)

    with open('gazetteer/ua.txt', 'w') as f:
        for name in names:
            f.write(name + '\n')
