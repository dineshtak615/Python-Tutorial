# from functools import reduce
# from math import gcd as _gcd
# def gcd(nums):
#   return reduce(_gcd, nums)
# nums = [336, 360]
# print("GCD of",','.join(str(e) for e in nums))
# print(gcd(nums))
# nums = [12, 17]
# print("GCD of",','.join(str(e) for e in nums))
# print(gcd(nums))
# nums = [4, 6]
# print("GCD of",','.join(str(e) for e in nums))
# print(gcd(nums))
# nums = [24, 30, 36]
# print("GCD of",','.join(str(e) for e in nums))
# print(gcd(nums))/

def gcd(x, y):
 z = x % y
 while z:
   x = y
   y = z
   z = x % y
 return y
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

