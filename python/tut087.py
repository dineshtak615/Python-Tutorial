# multiprocessing in python
import multiprocessing
import requests
import concurrent.futures

# from concurrent.futures import ProcessPoolExecutor


def downlowadfile(url, name):
    print(f'start downloding {name}')
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f'finished downloding {name}')


url = "https://picsum.photos/2000/3000"
if __name__ == '__main__':

#     pros=[]
#     for i in range(5000):
#         # downlowadfile(url, i)
#         p=multiprocessing.Process(target=downlowadfile,args=[url,i])
#         p.start()
#         pros.append(p)


#     for p in pros:
#         p.join()
 def pool():
   with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(6)]
    l2 = [i for i in range(6)]
    results = executor.map(downlowadfile, l1, l2)
    for r in results:
        print(r)
 pool()
    