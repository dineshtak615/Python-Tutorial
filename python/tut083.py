# ex 10
import requests
import json
query=input('what  type of news are you intersted in ?')
url=f"https://newsapi.org/v2/everything?q=tesla&from={query}2023-03-27&sortBy=publishedAt&apiKey=API_KEY"
r=requests.get(url)
news=json.loads(r.text)

# print(news,type(news))

for article in news ['articles']:
    print(article["title"])
    print(article["description"])
    print("----------------------")