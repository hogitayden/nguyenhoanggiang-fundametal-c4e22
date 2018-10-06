# pokemon = {
#     'name': 'pikachu',
#     'owner': 'Ash'
# }

# key = input('Enter your key ')
# value = input('Enter your value ')

# pokemon[key] = value
# print(pokemon)

pokemon = {
    'name': 'pikachu',
    'owner': 'Ash'
}

text = input('Enter new item ')
pair = text.split(",") #hàm tách chữ 
# key = pair[0]
# value = pair[1]
key, value = pair

pokemon[key] = value
print(pokemon)