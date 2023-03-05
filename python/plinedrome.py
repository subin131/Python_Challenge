num=int(input("Enter the 5 digit number: "))
#storing the number in temp variable
temp=num
reminder=0

while(num>0):
    a=num%10
    reminder=reminder*10+a
    num=num//10
   
#checking the condition 
if(temp==reminder):
     print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
    
    
