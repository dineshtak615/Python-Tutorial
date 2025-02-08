# STATIC METHOD         IT DONOT BELONG TO INTANTANCE AND CLASS 
class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod # don't use self argument
    def add(a,b):
        return a+b
    
a=math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(math.add(3,7))

# or
print(a.add(7,0))