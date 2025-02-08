# asyncio in python 
import time 
import asyncio
import requests

async def function1():
    url='http://nesssi.cacr.caltech.edu/cgi-bin/getmulticonedb_release2.cgi/post'
    files={'files': open('e.txt','rb')}
    values={'upload_file' : 'e.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}
    r=requests.post(url,files=files,data=values)
    # await  asyncio.sleep(1)
    # time.sleep(3)
    print("fun1")
    return "harry"
 
async def function2():
    url='http://nesssi.cacr.caltech.edu/cgi-bin/getmulticonedb_release2.cgi/post'
    files={'files': open('file2.txt','rb')}
    values={'upload_file' : 'file2.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}
    r=requests.post(url,files=files,data=values)

    # await  asyncio.sleep(1)
    # time.sleep(2)
    print("fun2")
    return 0

async def function3():
    url='http://nesssi.cacr.caltech.edu/cgi-bin/getmulticonedb_release2.cgi/post'
    files={'files': open('file3.txt','rb')}
    values={'upload_file' : 'file3.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}
    r=requests.post(url,files=files,data=values)
    # await  asyncio.sleep(1)
    # time.sleep(3)
    print("fun3")
async def main():
#   l=await asyncio.gather(
#        function1(),
#        function2(),
#        function3(),
#   )
#   print(l)
    



    task =asyncio.create_task(function1())
    await   function1()
    await   function2()
    await   function3()
asyncio.run(main())    