def f1(i=5,j=7):
    if((i:=7) ==7):
        i=i+j
        j=i+j
    else: 
        return i-2
def output(m=5):
    for i in range(m):
     print(f1(i,m-1),'@', end=" ")  
     print()       
output(6)
output()
output(5)

































