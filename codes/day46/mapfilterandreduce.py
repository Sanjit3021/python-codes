#MAP
def cube(x):
    return x*x*x

l=[1,2,3,4,5,6]
# newl=[]
# for i in l:
#     newl.append(cube(i))

newl=list(map(cube,l))

print(newl)


#FILTER
def fil_func(a):
    return a>2
newnl=list(filter(fil_func,l))
print(newnl)

#REDUCE
from functools import reduce
n=[1,2,3,4,5]
def mysum(x,y):
    return x+y
sum=reduce(mysum,n)
print(sum)