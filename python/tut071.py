# single inheritance in python

class animals:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("sound make by animals")
class dog(animals):
    def  __init__(self,name , breed):
        # animals.__init__(self,name,species="dog")
        self.breed=breed
    def make_sound(self):
        print("bark")

d=dog("cat","doggerman")
d.make_sound()


a=animals("cat","cat")
a.make_sound()