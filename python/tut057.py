# inheritance(single) in python
class employee:
    def __init__(self , id ,name):
        self.name=name
        self.id=id
 
    def showdetail(self):
         print(f"the name of employee {self.id} is {self.name}") 
            

class programmer(employee):# inheritance  by employeee class
    def showlanguage(self):
        print("the default language is python")


# e1=employee("rohan das", 400)         
# e1.showdetail()        
e2=programmer("danish",534)
e2.showlanguage()