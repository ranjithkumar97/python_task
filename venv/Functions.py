def ranjith():
    a=12
    b=45
    return a*b
c=ranjith()
print(c)

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist )

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print( "Values inside the function: ", mylist)
   return

a=['ranjith','santhosh','karthi','selvi']
itr=__iter__(a)
print(itr)


