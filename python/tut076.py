# creating command in python
import argparse
import requests
def download_file(url,local_filename):
# note the stream=true  parameterbelow

  with requests.get(url,stream=True) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192):
        # if have chunk encoded reponse uncommmed if 
        # and set chunk_size parameter to none
        # if chunk:
        f.write(chunk)
    return local_filename
  
parser=argparse.ArgumentParser()
# add commad line arguments
parser.add_argument("url",help="url of the file to downlond")
parser.add_argument("output ",help="by which name do you want to save your file")

args=parser.parse_args()

# use the arguments in your code
print(args.url)
print(args.output)
download_file(args.url,args.output)


