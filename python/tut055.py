# DEC0RATORS IN PYTHON

def greet(fx):
 def mfx(*a,**kwargs):
    print("goood morning ")
    fx(*a,**kwargs)
    print("thanks for using this function ")
 return mfx
    
# @greet
def hello():
  print("hello world ")  
 

# greet(hello)()

@greet
def add(x,y):
   print(x+y)

add(1,3)
