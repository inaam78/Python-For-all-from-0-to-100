a=int(input("enter your age: "))
# if elif else ladder
if (a>=18):
    print("you are eligible to vote")
elif(a==0):
    print("you are not born yet")
elif(a>0 and a<18):
    print("you are not eligible to vote")
else:
    print("you are not eligible to vote")