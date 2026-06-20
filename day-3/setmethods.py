set1={10,20,30,40}
set2={20,30,40}
set1.add(50)
print(set1)
set1.remove(30)
print(set1)
set1.update([70])
print(set1)
set3=set1.copy()
print(set3)
print(set1.difference(set2))
print(set1.difference_update(set2))
print(set1)
print(set1.union(set2))
print(set1)
print(set2)

