# Add two objects if both objects are an integer type
def addnum(a,b):
    if not( isinstance(a,int) and isinstance(b ,int) ):
        return "it is must be intger"
    return a+b

print(addnum(12,8))
print(addnum(122,44.4))