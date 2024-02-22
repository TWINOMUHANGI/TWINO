name = input("Enter name: ")
distance = int(input("Enter distance covered: "))


if distance <10:
    rate = 5000
elif distance <=50: 
    rate = 10000
elif distance >50:
    rate = 15000
    
bill = distance * rate
print(f"rate:\t{rate}\nbill:\t{bill}")