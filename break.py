from os import system
secrete_username = "adminn"
secrete_password = "user12345"
login_attempts = 0
limit = 3
while login_attempts <limit:
    username = input("Username: ")
    password = input("Password: ")
    if username == secrete_username and password == secrete_password:
        print("welcome to URA")
        break
    else:
        system("cls")
        print("Invalid Username and or Password")
    login_attempts +=1
else:
    print("you have exceeded the limit\n\n\tprog ended")
    
       
       
