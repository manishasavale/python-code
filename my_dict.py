
# Progs and their albums
progs = {'Yes': ['Close To The Edge','Fragile'],
    'Genesis': ['Foxrot', 'The Nursery Crime'],
    'ELP': ['Brain Salad Surgery']}

# More progs
progs['King Crimson'] = ['Red', 'Discipline']

# items() rerurns a list of tuples with key and value
for prog, albums in progs.items():
    print(prog, '=>', albums)

# If there is 'ELP', removes
if 'ELP' in progs:
    del progs['ELP']


print(progs)

for key, value in progs.items():
     print(key, '=>', value)

for key in progs.keys():
    print(key)

for value in progs.values():
    print(value)
