#using input function
def greater():
    a=int(input("Enter First Number : "))
    b=int(input("Enter Second Number : "))
    c=int(input("Enter Third Number : "))
    if (a>b) and (a>c):
        print(f"{a} is Greater")
    elif (b>a) and (b>c):
        print(f"{b} is Greater")
    else:
        print(f"{c} is Greater")
greater()
#using return statement with agruments
def great(a, b, c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    else:
        return c
result=great(10, 20, 30)
print(f"{result} is Greater")