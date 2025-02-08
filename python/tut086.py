# multithreading in python for use somethings download parallely
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# indicates some task being dones


def func(seconds):
    time.sleep(seconds)
    print(f"sleeping for {seconds} seconds")
    return seconds


def main():
    time1 = time.perf_counter()

# time1=time.perf_counter()
# # normal code
# func(4)
# func(3)
# func(1)
# time2=time.perf_counter()
# print(time2-time1)


# time1=time.perf_counter()
# t1=threading.Thread(target=func , args=[4])
# t2=threading.Thread(target=func , args=[5])
# t3=threading.Thread(target=func , args=[45])

# t1.start()
# t2.start()
# t3.start()

# t1.join() # frist(t1) is end then t2  is start
# t2.join()
# t3.join()
# calculating time
# time2=time.perf_counter()
# print(time2-time1)# same code in use therading

def poolingdemo():
    with ThreadPoolExecutor() as executor:
        #  future1=executor.submit(func,4)
        #  print(future1.result())

        #  future2=executor.submit(func,3)
        #  print(future2.result())

        #  future3=executor.submit(func,1)
        #  print(future3.result())
        l = [1, 3, 6, 6, 6]
        results = executor.map(func, l)
        for result in results:
            print(result)


poolingdemo()
