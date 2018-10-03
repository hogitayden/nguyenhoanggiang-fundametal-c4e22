items = ['bm Hoi An', 'bm Da Nang', 'bm Sai Gon']
print(*items, sep = ', ')
n = int(input('Where to change? '))
m = input('Change to what? ')
items[n-1] = m
print(*items, sep = ', ')