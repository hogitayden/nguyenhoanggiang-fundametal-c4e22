prices = {}
prices['banana'] = 4
prices['apple'] = 2
prices['orange'] = 1.5
prices['pear'] = 3
print(prices)

stock = {}
stock['banana'] = 6
stock['apple'] = 0
stock['orange'] = 32
stock['pear'] = 15

print(stock)
print()

for key, value in prices.items() and stock.items():
    print(key)
    print('price:', prices[key])
    print('stock:', stock[key])
    print()

total = 0
print('Value each fruit in cart: ')
for key, value in prices.items() and stock.items():
    total += prices[key]*stock[key]
    print(key, end=': ')
    print(prices[key]*stock[key])
print()
print("Total pocket's value: ", total)