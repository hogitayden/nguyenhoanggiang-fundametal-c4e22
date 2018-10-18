from generate_quiz import *
count = 0

while True:
    quiz = generate_quiz()
    x, op, y, r, error = quiz
    print('{0} {1} {2} = {3}'.format(x, op, y, r))
    ans = input("(T/F)? ").upper()
    #neu khong dung error thi dung if r == seasons(x, y, op):
    if error == 0: 
        if ans == "T":
            print("Yay")
            count += 1
        else:
            print("nah")
            print('point = ', count)
            break
    else:
        if ans == "F":
            print("Yay")
            count += 1
        else:
            print("nah")
            print('point = ', count)
            break