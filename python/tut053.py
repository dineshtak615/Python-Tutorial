# 00ps 
class person:
    name ="harry"
    occupation="soft developer"
    networth=10000
    def info(self):
        print(f"{self.name} is a {self.occupation} his networth {self.networth}")

    
a=person()
b=person()
c=person()#it is take default value isetlf
# b.name="manish"
# b.occupation="video editor"
# b.networth=20000000000000000000000000000000000000000000000000000000000000000000000000000022222222222200000000000000000200
a.name="harry"

print(a.name)
a.name="danish"  
print(a.name)
a.occupation="accountant"
a.networth=11111111111111111111113333333333333333333331111111111111111111111333333333333122222222222222222222222222222212
print(a.name, 
      a.occupation)

a.info()
# b.info()
# c.info()