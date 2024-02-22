### login program
saved_username = "brezz@ppg"
saved_password = "boss"

user_name = input("Username:\t")
password = input("Password:\t")

if user_name == saved_username and password == saved_password:
    print("login successfull")
else:
    print("invalid initials")
    
    