
# set function
# s1={1,2,5,6}
# s2={3,6,7}
# print(s2.union(s1))
# s1.update(s2)
# print(s1,s2)
# print(s1)

# cities={"tokyo","madrid","berlin","delhi"}
# cities2={"tokyo","seoul","kabul","madrid"}

# cities3=cities.intersection(cities2)
# print(cities3)
# cities.intersection_update(cities2)
# print(cities)

cities={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}

cities3=cities.symmetric_difference(cities2)
print(cities3)
cities.symmetric_difference_update(cities2)
print(cities)

# cities={"tokyo","madrid","berlin","delhi"}
# cities2={"tokyo","seoul","kabul","madrid"}

# cities3=cities.difference(cities2)
# print(cities3)
# cities.difference_update(cities2)
# print(cities)

# cities={"tokyo3","madrid4","berlin","delhi"}
# cities2={"tokyo","seoul","kabul","madrid"}

# print(cities.isdisjoint(cities2))

# cities={"tokyo","madrid","berlin","delhi"}
# cities2={"tokyo","seoul","kabul","madrid"}
# cites3={"tokyo","madrid","berlin"}
# print(cities.issuperset(cites3))

# print(cites3.issubset(cities))

# cities={"tokyo","madrid","berlin","delhi"}
# cities.add("tantwas")
# print(cities)
# cities.update()
# print(cities)

# cities.remove("tantwas")
# print(cities)
# cities.discard("tokyo")
# print(cities)


# cities={"tokyo","madrid","berlin","delhi"}

# del cities

# cities={"tokyo","madrid","berlin","delhi"}
# cities.clear()
# print(cities)

cities={"tokyo","madrid","berlin","delhi"}

if "tokyo" in cities:
    print("tokyo is present")
else:
    print("tokyo is absent")    





