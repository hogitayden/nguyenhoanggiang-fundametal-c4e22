items = ['bm Hoi An', 'bm Da Nang', 'bm Sai Gon']
print(*items, sep = ', ')
n = int(input('curren number of dishes to update? '))
m = input('which dishes to update? ')
items[n-1] = m
print(*items, sep = ', ')