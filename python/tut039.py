# enumerate function in python

# marks  =[12,56,32,98,12,45 ,1,4]
# index=0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("harry ,  awesommme ")
#     index+=1

# 


marks  =[12,56,32,98,12,45 ,1,4]

# for mark, index in enumerate( marks):
# for index,mark in enumerate( marks):
#     print(mark)
#     if(index == 3):
#         print("harry ,  awesommme ")
    

marks  =[12,56,32,98,12,45 ,1,4]

# for mark, index in enumerate( marks):
for index,mark in enumerate( marks,start=-1):
    print(mark)
    if(index == 3):
        print("harry ,  awesommme ")
    





