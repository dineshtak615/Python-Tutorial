#  map ,filter and reduce in python this is all higher order function 

def cube(x):
    return x*x*x

print(cube(2))

l=[1,2,4,6,4,3]
# # newl=[]
# for item in l:
#     newl.append(cube(item))

# map  easily use 
# newl=list(map(lambda x:x*x*x,l))
# newl=list(map(cube,l)) 
# print(newl)



# FILTER
# def filter_function(a):
#   return a>2
# newnewl=list(filter(filter_function,l))
# print(newnewl)

# REDUCE
 
from functools import reduce
l=[1,2,4,6,4,3]  # 1+2=3, l=[3,4,6,4,3] then 3+4 =7, l= [7,6,4,3] then 7+6=15
def mysum(x,y):
    return x+y
# 
lma= lambda x,y: x+y

sum=reduce(lma,l)
print(sum)




