countries = ("spain","italy","India","Germany")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="finland"
countries=tuple(temp)
print(countries)
tuple1=(0,1,2,3,2,3,1,2,1,3,3,2,1)
res=tuple1.count(3)
res=tuple1.index(3)
print("count of 3 in tuple1 is:",res)