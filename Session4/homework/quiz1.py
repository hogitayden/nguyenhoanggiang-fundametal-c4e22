q1 ={
    'cmd': 'Answer the following algebra question:',
    'ques': 'If x = 8, then what is the value of 4(x + 3)?',
    'ans': ['1. 35', '2. 36', '3. 40', '4. 44'],
    'correct ans': 4,
}

q2 = {
    'cmd': 'Estimate this answer (exact caculation not needed):',
    'ques': 'Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?',
    'ans': ['1. About 55', '2. About 65', '3. About 75', '4. About 85'],
    'correct ans': 2,
}

test = [q1, q2]
score = 0

for i in range(len(test)):
    print(test[i]['cmd'])
    print(test[i]['ques'])
    print(*test[i]['ans'], sep ='\n')
    print()
  
    ans = input('Your choice? ')
    if ans.isdigit():
        ans = int(ans)
        if ans <5:
            if ans == test[i]['correct ans']:
                print('Bingo')
                score += 1
            else:
                print(':(')
                print('score:',score)
        else:
            print('No more than 4 choices, baby!')
            print('score:',score)
    else:
        print('wrong too far')
        print('score:',score)

print('You correctly answer', score, 'out of 2 questions')