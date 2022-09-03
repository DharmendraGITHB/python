# RealPython
# Decorator as name suggest that which allows programmers to modify the behaviour of a function or class


def decorator(func):
  def wrapper():
    print("before function call")
    
    func()                #it reference to say_hello()
    
    print("after function call")
   
  return wrapper

def say_hello():
  print("heelllo")
  
say_hello = decorator(say_hello)    

say_hello()   #it reference to wrapper function first
 
