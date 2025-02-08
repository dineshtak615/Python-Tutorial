# seek and tell function in io file
# with open('myfile4.txt','r') as f:
#     print(type(f))
#     # move to the 10th byte in file
#     f.seek(10)

#     # read the next 5 byte 
#     print(f.tell()) #it is function use the track the current position in string 
#     data=f.read(5) #we can use the nagative number 
#     print(data)

# truncate( ) method 
with open('simple.txt','w') as f:
    f.write("hello world3")
    f.truncate(3) # it is remove  the all character take only  3 character in frint

with open('simple.txt','r') as f:
    print(f.read())



