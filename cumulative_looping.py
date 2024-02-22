counter = 0
total = 0
while counter <10: 
    number = int(input(f"Enter Number: {counter}:"))
    total = total + number
    counter +=1
    
print(f"\n\t Total:{total}")