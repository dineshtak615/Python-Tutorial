# match case statement in python
# import os

# print("hello world from ......")
# os.system("python --version ")

x=int(input("enter the value of x:"))
#  xi si variable to match
match  x:
    #  if x is zero
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print("is not 90")
    case _ if x!=80:
        print("is not 80 ")
    case _ :
        print(x)    
                   
    















