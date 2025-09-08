uname=input("name:")
password=int(input("password:"))

if uname=="ashu" and password==9100:
             print("welcome")
else:
    print("invalid username and password")
    

num=int(input("Enter any number "))
last_digit=num%10
r=last_digit%3
if r==0:
    print("Divisible")
else:
    print("Not divisible")



amount=int(input("Amount :"))
if (amount%500)==0:
    print("Mulitples of 500")
else:
    print("Not Multiples of 500")
