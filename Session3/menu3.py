items = ['Campucheer', 'Thailen','Turkey chicken']
print(*items, sep = '| ')

while True:
    i = int(input("Serial num of dishes? "))
    if i < 3:
        print(items[i - 1])
        break
    else:
        print("Sorry, we dun hav dis")

print(*items, sep = '\n')