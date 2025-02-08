import os

if(not os.path.exists("data")):
  os.mkdir("data")

for i in range(0, 100):
    # os.mkdir(f"data/day {i+1}")
    os.rename(f"data/day {i+1}", f"data/tutorial {i+1}"  ) # it is use for rename of folder 