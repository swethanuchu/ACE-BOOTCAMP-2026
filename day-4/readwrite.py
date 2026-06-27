f=open("/workspaces/ACE-BOOTCAMP-2026/day-6/test.txt","r+")
f.write("i love")
f.seek(0)
print(f.read())
print("file name",f.name)
print(f.tell())
print(f.closed)

with open("/workspaces/ACE-BOOTCAMP-2026/day-6/test.txt",'r') as f:
    print(f.read())
print(f.closed)