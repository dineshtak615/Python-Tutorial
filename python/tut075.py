# time module in python
import time
# def usingwhile():
#     i=0
#     while i<50:
#         i +=1
#         print(i)

# def usingfor():
#     for i in range(50):
#         print(i)        

# init =time.time()
# usingwhile()
# print(time.time()-init)

# init =time.time()
# usingfor()
# # print(t)
# print(time.time()-init )


# print(4)
# time.sleep(55)
# print("this is printed after 55 secondss")


t=time.localtime()
t=time.strftime("%y-%M-%d  %H:%M:%S",t )
print(t)