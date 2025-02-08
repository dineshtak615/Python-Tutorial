import os 
folders = os.listdir("data")

print(os.getcwd())
os.chdir("/users")
print(os.getcwd()) # here dirctre is change before  dir is  "data" aftre run this function the dir is  change  make new dir  "usres " 
print(folders)

# for folder in folders : # here dir is data so this for loop donot work  because new dir users 
#      print(folder)
#      print(os.listdir(f"data/{folder}"))    

for folder in folders : 
    print(folder)
    print(os.listdir(f"users/{folder}"))
    os.system