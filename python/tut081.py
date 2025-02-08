# geneartor in python  it is genrate value on fly on

def my_genrator():
    for i in range(50):
        yield i


gen=  my_genrator()

print(next(gen))      
print(next(gen))      
print(next(gen))      

for j in gen:
    j=j+1
    print(j)