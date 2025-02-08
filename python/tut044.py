# x=4
# print(x)
# def hello():
#     x=5
#     print(f"the local  x is {x}")
#     print(x)
#     print("hello harry")

# print(f"the global  x is {x}")
# hello()
# print(f"the global  x is {x}")

x=10 #global variable
def my_func():
     global x # here global variable value is change and update new value of x in function
     
     x=4
     y=5 #  local varable
     print(y)

my_func()
print(x)
# print(y) this will cause an error because y is a local variable and is not accessiable outside of the function


