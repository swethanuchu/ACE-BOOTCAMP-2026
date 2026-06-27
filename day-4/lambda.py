from functools import reduce 
slist=[1,2,3,4,5]
mlist=[2,3,4,5,6]
print(list(map(lambda x:x*x,slist)))
print(list(map(lambda y:y*y,mlist)))
print(list(filter(lambda val:val%2==0,slist)))
print(list(filter(lambda val:val%2==0,mlist)))
print(list(filter(lambda val:val%2!=0,slist)))
print(list(filter(lambda val:val%2!=0,mlist)))
#sum of all the elements in the list
print(reduce(lambda x,y:x+y,slist))
#product of all the elements in the list
print(reduce(lambda x,y:x*y,slist))
xlist=[["xyz",1],["pqr",3],["klm",2],["abc",4]]
print(list(sorted(slist)))
print(list(sorted(xlist,key=lambda x:x[1])))