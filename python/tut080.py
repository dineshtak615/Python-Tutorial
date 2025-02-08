import requests
# response=requests.get("https://www.codewithharry.com")
# print(response.text)


# url="https://jsonplaceholder.typicode.com/posts"

# data={
#     "title":'foo',
#     "body" :'bar',
#     "userid":12,

# }
# headers={
#     'content-type':'application/json;charset=UTF-8,'
# }

# response=requests.post(url,headers=headers,json=data)
# print(response.text)



from bs4 import BeautifulSoup

url="https://www.codewithharry.com/blogpostdjango-cheatsheet/"
r=requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
