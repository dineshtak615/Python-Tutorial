# mehtod overloading in python
class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def aera(self):
        return self.x*self.y  

class crical(shape):
     def __init__(self,radius):
         self.radius=radius
         super().__init__(radius,radius) # radius change the value of self.x and self.y
     def  aera(self):
         return 3.14*super().aera()     




rec=shape(3,4)
print(rec.aera())

c=crical(5)
print(c.aera())
