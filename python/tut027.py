# recursion 

'''
factorial(7)=7*6*5*4*3*2*1
factorial(6)=6*5*4*3*2*1


factorial(n)=n*factorial(n-1)
'''
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))  
print(factorial(68))  
 
 # 4 *factorial(3)
#  4*3*factorial(2)
# 4*3*2*factorial(1)
#  this logic behind  in this program ok