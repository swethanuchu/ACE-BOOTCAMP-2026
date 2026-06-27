try:
    a=int(input("Enter first value"))
    b=int(input("Enter second value"))
    print("try:try block is executing")
    if b%2==0:
        raise Exception
except ZeroDivisionError as zd:
    print(zd)
except Exception as e:
    print("Division by evens are not allowed10")
else:
    print("catch:try block is executed")
finally:
    print("finally:going to close")