# class method  as alternative constructor in python
class employee:
    def __init__(self,name,salary,r):
        self.name=name
        self.salary=salary
        self.r=r

    @classmethod # classmethod as alternative using a string 
    def fromstr(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1]),string.split("-")[2])

# e1=employee("harry",12000,6)
# print(e1.name)    #----->  it is making by  useing constructor
# print(e1.salary) 

string="jonh-12000-helllo" 
e2=employee.fromstr(string)
print(e2.name)
print(e2.salary)
print(e2.r)