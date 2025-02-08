# #  io file  handling  in python
# f=open('myfile1.txt','r') # 'r' mode is default 
# # print(f)
# text=f.read()
# print(text)
# f.close()
# # 'w' this is write mode either in 'w' mode the file not exsit  this mode itself generate  that file like this f=open("myfile1.txt",'w')
# # 'rb'  for binaray from

# write a file
# f=open('myfile.txt','a')
# f.write("hello,  world!")
# f.close()

# with open('myflie.txt','a') as f:

#     f.write("hey i am inside with")


# # readline method  "it is use for line to line access file "
# f=open('myflie.txt','r')
# while True:
    
#     line=f.readline()
#     if not line:
#         print(line ,type(line))
#         break
#     m1=int(line.split(",")[0])# do the typecasting because in file data is in string
#     m2=int(line.split(",")[1])
#     m3=int(line.split(",")[2])
#     print(f"markm of studend 1 in maths is :{m1}")
#     print(f"markm of studend 2 in physics is :{m2}")
#     print(f"markm of studend 3 in pps is :{m3}")
    
#     print(line) 


# WRITELINE METHOD 
f=open('myfile3.txt','w')
lines=['line1\n','line2\n ','line3\n']
f.writelines(lines)
f.close
