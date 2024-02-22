print("****Workers****")
code = int(input("""
 1.Manager\n
 2.Hourly workers\n
 3.Commission workers\n
 4.Piece Workers            
"""))




if code == 1:
    fixed_weekly_salary = 20000
    wage = fixed_weekly_salary
    print(wage)
    
elif code == 2:
    
    hours_worked = int(input("Enter Hours:\t"))
    print = ("hours_worked:\n ")
    normal_time = 40
    normal_time_pay = 300 * hours_worked 
    if hours_worked <= 40:  
              
       hourly_work  = normal_time_pay
       print(hourly_work)
        
    else:
        over_time = hours_worked - normal_time
        over_time_pay =(1.5*300) * over_time  
        extra_time = over_time_pay + normal_time_pay
        print(extra_time)
               
elif code == 3:
    sales = int(input("Enter Gross sales:\t"))
    print("sales:\n ")
    commission = 0.0057
    commission_work= 250 + (commission * sales)
    print(commission_work)
         
elif code == 4:
    item = input("Enter item name:\n")
    item_number = input("Enter item number:\n ")
    print = ("item:\n ")
    print("item_number:\n ")
    total_item = item * item_number
    total_amount = 200 * total_item 
    

    

    
    
       
    
    