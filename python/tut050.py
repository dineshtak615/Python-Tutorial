# lambda  function in python it  is a  small anonymomus function without name
# it is use for write a  single exepretion  like this
# def double(x):
#     return x*2
# print(double(5))
# this fuction like use lambda function
# double =lambda x: x*2
# cude=lambda x:x*x*x
# avg= lambda x,y,z :(x+y+z)
# print(double(5))
# print(cude(5))
# print(avg(45,6,6))

def appal(fx, value):
    return fx(value)


print(appal(lambda x: x * x, 2))
