#Program to calculate the employee owe any overtime or not.
#taking input as how many hours the user worked in a week
hours=int(input("Enter the worked hour per week: "))

#taking the hourly wages 
wages=int(input("Enter the hourly wages: "))

total_amt=wages*hours
if hours<40:
    print(f"The total amount after working {hours}  hours with hourly {wages} is {total_amt}. ")
    
else:
    extra_hours=hours-40
    new_wages=wages+wages*0.2
    additional_amt=extra_hours*new_wages
    total_amt=(40*wages)+additional_amt
    print(f"The additional amount is {additional_amt} and the total amount is {total_amt}. ")