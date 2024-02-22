gender = input("Enter your gender:\t")
cgpa = float(input("Enter CGPA:"))
award = ""


cgpa_class = "None"

if cgpa<=1.9:
    
    cgpa_class = "Fail"
elif cgpa<=2.4:
    
    cgpa_class = "Pass"
elif cgpa<=3.5:
    cgpa_class= "Second class lower"
elif cgpa<=4.4:
    cgpa_class = "Seconds class upper"
elif cgpa<=5.0:
    cgpa_class = "First class"
    if cgpa_class == "First class":
        if gender == "male":
            award = "Gold medal"
        if gender == "female":
            award = "Gold medal + laptop"
    
        
    
else:
    print("Invalid ") 
print(f"CGPA:\t{cgpa}\nCGPA Class:\t{cgpa_class}\nAward:\t{award}\t")
    
