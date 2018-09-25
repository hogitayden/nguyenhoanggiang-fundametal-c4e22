yob =  int(input("Yeah of birth? "))
age = 2018 - yob
print(age)

if age < 10: 
    print("baby")
elif age < 18:
    print("teenager")
else:
    print("not a baby")

