# exesices 2
import time
timestamp=time.strftime('%H:%M:%S')
hour=time.strftime('%H')
hour=int(input("enter the  hour  :"))
print(hour)

if(hour>=0 and hour<12):
    print("good morning sir")

elif(hour>=12 and hour<17):
  print("good afternoon sir!")

if(hour>=17 and hour<0):        
    print("goood morinng sir")





print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)


