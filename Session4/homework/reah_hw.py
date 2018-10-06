inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

k = 'pocket'
v = ['seashell', 'strange berry', 'lint']

inventory[k] = v
for k, v in inventory.items():
    print(k,v, sep=': ')
print()

inventory['backpack'].remove('dagger')
print(*inventory['backpack'], sep =', ')
print()

inventory['gold'] += 50
print(inventory['gold'])