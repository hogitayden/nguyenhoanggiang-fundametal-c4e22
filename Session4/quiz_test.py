print('Answer the following algebra question:')
print('If x = 8, then what is the value of 4(x + 3)')
print('1. 35')
print('2. 36')
print('3. 40')
print('4. 44')

while True:
    ans = input("What your answer? ")
    print('Your choice: ', ans)
    if ans.isdigit():
        ans = int(ans)
        if ans == 1 or ans == 2 or ans == 3 or ans == 4:
            if ans == 4:
                print('Bingo')
                break
            else:
                print(':(')
        else:
            print('Choose again')
    else:
        print('choose a number')