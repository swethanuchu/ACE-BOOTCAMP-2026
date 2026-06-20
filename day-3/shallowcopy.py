import sys
my_list=[]
print(list.__sizeof__(my_list))
print(sys.getsizeof(my_list))
for i in range(10):
    my_list.append(i)
    print(list.__sizeof__(my_list))
print(my_list)
s_list=my_list
s_list[3]=14
print(f"Shallow list:{s_list}")
print(f"Original list:{my_list}")
