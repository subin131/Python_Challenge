#welcome to my system
print("Welcome to our System")
#taking input for total friends
total_friends=int(input("Enter number of friends: "))
#taking total bill amount
total_bill=int(input("Enter the total bill amount: "))
#tax added amount
tax_amt=total_bill+total_bill*0.20
#split into the friends
split_bill=tax_amt/total_friends
#print the result
print(split_bill)