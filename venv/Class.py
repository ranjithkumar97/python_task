import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

def roy():
    x=int(input('enter the 1st number'))
    y=int(input('enter the 2nd nukmber'))
    z=x*y
    print(z)
    return x,y,z
ranjith()
roy()

def my_function(x):
  return list( dict.fromkeys(x) )

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)
