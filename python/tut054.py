# constructors in python
class person:# in class defind a "def  info(self ) :" the self is must
    def __init__(self ,name,occ,networth):# THIS IS A CONSTRUCTOR  IT IS WRITE DOWN "__init__(self) :  it is return   none 
        print("hey i am a person")
        self.name= name
        self.occ=occ
        self.networth=networth

    def info(self ):
        print(f"{self.name} is a {self.occ}  his networth  {self.networth} ")


    # name="harry"
    # occ="sfot developer" #------> this things not use because we can  use constructor  
    # networth=90000000000000000

# a=person("divya","HR","networth")
b=person("harry","developer","networth")
# c=person("x","y","u") #--->self is use as argument  inn constructor 

# print(a.name)
# a.name="divya"
# a.occ="HR"
# a.info()
# b.info()
# c.info()