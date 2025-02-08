num = int(input("enter  the value of number : "))

if(num < 18):
    print("num is positive")
elif(num > 0):
    if(num <= 10):
        print("number is b/w 1-10")
    elif(num > 10 and num <= 20):
         print(" num er 11-20")
    else:
       print("num is greater  than 20")
else:
  print("number is zero ")
