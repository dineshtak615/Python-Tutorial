# python class method
class employee:
    company="apple"
    name="harry"

    def show(self):
    
        print(f"the name is    { self.name} and company is { self.company }") 

    @classmethod # it is notting but it change  class variable name
    def changecompany(cls,newcompany):
        cls.company=newcompany    

e1=employee()
e1.name="harry"
print(employee.company)
e1.show
e1.changecompany('tesla')       
e1.show()
print(employee.company)