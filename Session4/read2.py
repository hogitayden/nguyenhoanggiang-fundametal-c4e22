person = {
    'name': 'Hogi',
    'age': 23,
    'talent': 'raider'
}
# while True:
#     key = input('What key you want? ')
#     if key == 'name' or key == 'age' or key == 'talent':
#         print(person[key])
#         break
#     else:
#         print('Again! ')

while True:
    key = input('What key you want? ')

    if key in person:
        print(person[key])
        break
    else:
        print('Not found')      