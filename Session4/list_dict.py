
#khai báo p1, p2 là biến nhỏ trước, khai báo list to sau rồi cho thẳng p1 p2 vào list

person_list = [
  {
    'name': 'Hogi',
    'age': 23,
  }, 
  {
    'name': 'Hato',
    'age': 24,
  }
]   #format có tên gọi khác là JSON (format web)


# person_list.append(p1) 
# person_list.append(p2) #lưu nhiều dict vào list: xài .extend


print(person_list)

# person_list[0] = {
#     'name': 'God',
#     'age': 1000,
# }

# person_list.pop(0)

# p = person_list[0]
# print(person_list[0]['age'])

for p in person_list:
    print(p['age'])
