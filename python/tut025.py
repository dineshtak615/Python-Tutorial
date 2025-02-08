# f - string
letter="hey my is {0} and i am from {1}"
country="india"
name="harry"
print(letter.format(country,name))
print(letter.format(name,country))
# same things by f string
country="india"
name="harry"

print(f"hey my is {name} and i am from {country}") # this type called f string 

txt="for only {price:.2f} dollers!"
print(txt.format(price=49.555))

price=588.000 # this is  f string 
print(f"for only {price} dollers !")

print(type(f"{2*30}"))

print(f"hey my is {{name}} and i am from {{country}}") # this type called f string 


