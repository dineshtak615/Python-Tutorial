#recursion  of fibonacci serise

'''
f(0)=0
f(1)=1
 f(2)=f(1)+f(0)

f(n)=f(n-1)+f(n-2)

'''

def fibonacci(n):
    if(n==0 or n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(3))  
print(fibonacci(45))  