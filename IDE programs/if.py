if 10>5:
    print("hello")


if 20<50:
    print("bye")
    
if True:
    print("PYTHON")
else:
    print("JAVA")

if False:
    print("hello")
else:
    print("Bye")
    

name=input("Enter Name :")
age=int(input("Enter Age :"))
if age>=18:
    print(name,"elg to vote")
else:
    print(name,"not elg to vote")



import random
name=input("name:")
otp=random.randint(1000,99999)
print("Login with",otp,"number")
iotp=int(input ("input OTP nnumber:"))
if otp==iotp:
         print("welcome")
else:
    print("Wrong OTP number")
    
