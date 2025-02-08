# regular expressions in python
import re 

pattern= r"[A-z]+yclone"
text='''
oading configuration
Done loading configuration 

Cyclone Dyclone 

'''

# match=re.search(pattern,text)
# print(match)

matchs=re.finditer(pattern,text)
for match in matchs:
    print(match.span())
    print(type(match.span()))
    print(text[match.span()[0]:match.span()[1]])
