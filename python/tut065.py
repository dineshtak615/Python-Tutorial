# dir ,__dict__ ,and help method in python
# x=[1,3,4]
# print(dir(x))
# print(x.__add__)


# __DICT__

class  person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1
p=person("john",30)  
print(p.__dict__)      


    #  help()

# print(help(str))
print(help(person))