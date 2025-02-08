# access modifiers in python  1.protect ,2.private ,3. public

#


class student:
    def __init__(self):
        self._name = "harry"


    def _fun(self):  # protect method
      return "hello"
    


class subject(student):  # inheritance class
    pass


obj = student()
obj1 = subject()
# print(dir(obj))

# calling by object of student class
print(obj._name)
print(obj._fun())

# calling by object of subject class
print(obj1._name)
print(obj1._fun())
