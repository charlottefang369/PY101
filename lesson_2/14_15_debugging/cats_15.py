import pdb

cats = []

for name in ('Powder', 'Sky', 'Cheddar', 'Cocoa'):
    pdb.set_trace()
    cats.append(name) #original erroneous code: cats + [name]

print(cats)

