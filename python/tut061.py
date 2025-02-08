# isinstance variable vs class variable in python
class employee :
    companyname="APPLE"
    #it is class variable
    no0femployee=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        employee.no0femployee +=1
    def showdetails(self):
         print(f"the name of the empolyee is {self.name} and the raise amount in {self.no0femployee}  sized {self.companyname} is {self.raise_amount}")
 
# employee.showdetails(emp1)
emp1=employee("harry")
emp1.raise_amount=0.03 #it is instance variable 
emp1.companyname="apple india"
emp1.showdetails()


print(employee.companyname)

emp2=employee("rohan")
emp2.raise_amount=0.09
emp2.companyname="gooogle"
emp2.showdetails()

