while True:
    my_password = input("Name your password? ")    
    if len(my_password) >= 8: #True
       
        if not my_password.isdigit():#True
           
            if not my_password.isupper(): 
                
                if not my_password.islower():
                    print("OK")
                    break
                else:
                    print("Wrong pw.")
            else:
                print("Need uppercase!")
        else:
            print("Not only digits! ")
    else:
        print("Not long enough.")
            
            
   

    