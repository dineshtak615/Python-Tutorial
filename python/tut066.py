# super keyword in  python  it is follow dry principal]
class employee :
    def __init__(self,name,id):
        self.name = name
        self.id=id


class programmer(employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id) # it super keyword not make new name and id super do itself

        self.lang=lang

rohan=employee("rohan",333,)        
harry=programmer("harry",455,"python")
print(harry.name)
print(harry.id)
print(harry.lang)
print(rohan.name)