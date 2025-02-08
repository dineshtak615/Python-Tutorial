# multiple  inheritance 
class employee:
    def __init__(self,name) :
        self.name=name
    def show(self):   
        print(f"the name of employee {self.name}")



class dencer:
   def __init__(self,dance) :
       self.dance=dance
   def  show(self):  
       print(f"the name of dance {self.dance}")



class dancerempolyee(employee,dencer): # we wiil change order of employee and dancer  
    def __init__(self, name,dance):
        self.name=(name)
        self.dance=dance

o=dancerempolyee("kathak","shivani")
print(o.dance)
print(o.name)
o.show()
print(dancerempolyee.mro())