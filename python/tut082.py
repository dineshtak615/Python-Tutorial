# function caching in python

import functools

import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 30")

print(fx(2))
print("done for 2")

print(fx(10))
print("done for 10")

print(fx(20))
print("done for 30")

print(fx(2))
print("done for 2") # this function not take time 

print(fx(10))
print("done for 10")

print(fx(49))
print("this function takes time")



