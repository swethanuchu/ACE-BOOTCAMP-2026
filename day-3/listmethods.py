my_list=[]

for i in range(5):
    element=int(input())
    my_list.insert(i,element)
print(my_list)
my_list.append(60)
print(my_list)
list1=my_list.copy()
print(list1)
my_list.reverse()
print(my_list)
print(my_list.index(30))
my_list.pop(2)
print(my_list)
print(my_list.count(3))
