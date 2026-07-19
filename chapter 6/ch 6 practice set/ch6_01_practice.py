a1=int(input("enter a1 : "))
a2=int(input("enter a2 : "))
a3=int(input("enter a3 : "))
a4=int(input("enter a4 : "))
if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greater")
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greater")
elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is greater")
elif(a4>a1 and a4>a2 and a4>a3):
    print("a4 is greater")
else:
    print("all are equal")