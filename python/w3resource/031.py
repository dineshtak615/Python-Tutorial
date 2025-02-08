#  Q.Return true if the two given integer values are equal or their sum or difference is 5
def nubtest(x,y):
    if x==y or x+y==5 or x-y ==5:
        return True
    else:
        return False
    
print(nubtest(7,2)    )
print(nubtest(3,4))