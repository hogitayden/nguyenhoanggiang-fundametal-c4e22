items = ['bm Hoi An', 'bm Da Nang', 'bm Sai Gon']
print(*items, sep = ', ')

n = input('which dishes you want to delete? ')
if n.isdigit():
    n = int(n)
    items.pop(n-1)
else:
    items.remove(n)
print(*items, sep = ', ')