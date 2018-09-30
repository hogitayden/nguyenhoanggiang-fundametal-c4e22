while True:
    yob_str = input("Enter dob? ")
    if yob_str.isdigit():
        yob = int(yob_str)
        age = 2018 - yob
        print(age)
        exit()
    else:
        print("Not a number")