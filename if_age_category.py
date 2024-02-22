birth_year = int(input("Enter your birth year:"))
current_year = 2014

age = current_year - birth_year
print(f"Your age is:{age}")
if age <=3:
    print("this is a baby")
elif age<=10:
    print("You are a Kid")
elif age <=20:
    print("you are a teenager")
elif age <=35:
    print("You are a youth") 
elif age <=50:
    print("You are a senior citzen")
else:
    print("you are an elder")