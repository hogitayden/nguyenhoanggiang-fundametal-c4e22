clothes = ['T-Shirt', 'Sweater', 'Bomber', 'Bikini']

while True:
    n = input('Welcome to our shop, what do you want (C, R, U, D, e)? ')
    if n == "R":
        print('Current collection', *clothes, sep =', ')
        
    elif n == "C":
        print(*clothes, sep=', ')
        while True:
            new_item = input('Add your new item (Jeans?) ')
            if new_item.isdigit():
                print("Enter right name, please!")
            else:
                clothes.append(new_item)
                print('New collection: ', end="")
                print(*clothes, sep =', ')
                break
                
    elif n == "U":
        print(*clothes, sep =', ')
        while True:
            pos = (input('Replace item number? '))
            if pos.isdigit():
                pos = int(pos)
                if pos <= len(clothes):
                    update_item = input('New item for updating (Skirt?) ')
                    clothes[pos-1] = update_item
                    print('New collection: ', end='')
                    print(*clothes, sep =', ')
                    break
                else:
                    print('Please choose number in range [1,', len(clothes), ']')
            else:
                print('Please enter a number!')

    elif n == "D":
        pos = 1
        for clothe in clothes:
            print(pos, clothe)
            pos += 1

        while True:
            pos = input('Which item you want to delete? ')
            if pos.isdigit():
                pos = int(pos)
                if pos <= len(clothes):
                    clothes.pop(pos-1)
                    print('New collection: ', end='')
                    print(*clothes, sep =', ')
                    break
                else:
                    print('Please choose number in range [1,', len(clothes),']')
            else:
                print('Please enter a number!')
        
    elif n == "e":
        print('Thanks, see you later!')
        exit()

    else:
        print('please choose C, R, U, D or e')
    
    