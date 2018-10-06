person = {
    'name': 'Hogi',
    'age': 23,
    'talent': 'raider'
}

print(person)

while True:
    action = input('Do you wanna Update (U) or Delete (D)? ')

    if "D": #tương đương với value == "D"
        while True: #để while True nó sẽ lặp lại tiếp hỏi D hay U
            key = input('Which key to delete? ')
            if key in person:
                del person[key]
                print(person)
                break
            else:
                print('Please choose name, age or talent. ')

    elif action == "U":
        while True:    
            key = input('Which key to update? ')
            if key in person:
                new_key = input('New key? ')
                person[key] = new_key
                print(person)
                break
            else:
                print('Please choose name, age or talent. ')
    else:
        print("Please enter U or D ! ")