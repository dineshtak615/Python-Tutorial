# exception(error handling  )handling in python
# a=input("enter  the number : ")
# print(f"multiplication table of {a} is :")

# try :    
#     for  i in range(1,11):
#      print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e :
#        print(e)

# print("some imp line of code ")
# print("end of program ")    

# a=input("enter  the number : ")
# print(f"multiplication table of {a} is :")

# try :    
#     for  i in range(1,11):
#      print(f"{int(a)} X {i} = {int(a)*i}")
# except :
#        print("invaid input!")

# print("some imp line of code ")
# print("end of program ")    


try :
    num= int(input(" enter the number :"))
    a=[6,7]
    print(a[num])
except ValueError :
    print("number entered is not an integer ")
except IndexError :
    print("index error")
except FloatingPointError:
     print("same type error ")
