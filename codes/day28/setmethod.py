s1={1,2,3,4,5,6,7}
s2={2,4,6,8,9}
s3=s1.union(s2)
s1.update(s2)
print(s3)
print(s1)
s3=s1.intersection(s2)
print(s3)
s1.intersection_update(s2)
print(s1)
s3=s1.symmetric_difference(s2)
print(s3)
s1.symmetric_difference_update(s2)
print(s1)
s3=s1.difference(s2)
print(s3)
s1.difference_update(s2)
print(s1)
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))