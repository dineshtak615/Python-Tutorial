# hybrid and hierarchical inherutance in python
# this all class are called hybrid  inheritance

# hybrid inheritance
class baseclass :
    pass



class derived1(baseclass):
    pass
class derived2(baseclass):
    pass

class derived3(derived1 ,derived2):
    pass


#  hierarchical inheritance 
# it is all are joint each either
class a:
    pass

class b(a):

    pass
class c(a):

 pass

class d(b):
    pass
class e(b):

    pass
class f(c):
    pass
class g(c):

 pass


