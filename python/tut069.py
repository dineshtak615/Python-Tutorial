import os
files=os.listdir('cultteredfolder')
i=1
for file in files:
   if file.endswith("ff01.png"):
       print(file)
       os.rename(f'cultteredfolder/{file}',f'cultterdfolder/{i}.png')    
       i=i+1
    
os.rename('cultteredfolder/f.txt','cultterdfolder/6.txt') 
