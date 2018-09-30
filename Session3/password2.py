while True:
    pwd = input("Enter: ")
    if len(pwd) < 8:
        print("Not long enoguh")
    elif pwd.isupper():
        print("Must contain letters")
    elif pwd.islower():
        print("Must contain both upper and lower letters")
    elif pwd.isdigit():
        print("Must contain both upper and lower letters")
    else:
        print("OK")
        exit()