# dictionaries in python

dic = {
        "harry":  "humen bening",
        "spoon":  "object",
        344:" danish",
        56:"manish"


}
# print(dic["harry"])
# print(dic[56])
print(type(dic))


info={"name":"karan","age":19,"eligiable":True}
print(info)
print(info["name"])# give the error
print(info.get("eligiable0"))  # it is give none
print(info.keys())# only give the keys
print(info.values()) #it is take the value of keys

for key in info.keys():
     print(info[key]) #this fun take the keys value 

for key in info.keys():
    print(f"the value corresponding to key {key}  is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"the value corrponding to the key {key } is {value }")


