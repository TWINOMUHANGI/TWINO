worker_name = input ("Your name is:")
task = input("Activity done:")
hours_worked = int(input("Hours worked:"))
RATE = int(3000)

wage = int(hours_worked * RATE)

meal_allowance = float(5 / 100) * RATE 
gross_wage = wage + meal_allowance 
tax = 5 / 100 * gross_wage
net_wage = gross_wage - tax
print(f"your name is: {worker_name} \nyour activity: {task} \nhours worked: {hours_worked} \nRate: {RATE} \nwage is: {wage} \nAllowance is: {meal_allowance} \nGross wage is: {gross_wage} \nTax: {tax} \nNet wage: {net_wage}")