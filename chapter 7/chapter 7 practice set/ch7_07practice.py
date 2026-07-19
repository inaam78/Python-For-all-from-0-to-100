# inverted right-angled triangle for n=5
# n=int(input("Enter a number: "))
# for i in range(n,0,-1):
#     print("*"*i)

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#   print(" " *(n-i)+"*"*(2*i-1))


# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#    print("*"*i)

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

# hollow square pattern
n=int(input("Enter a number: "))
for i in range(1,n+1):   # loop chalega 1 se n tak (rows k liye)
    if(i==1 or i==n):    # agar row pehli ya last ho
        print("*"*n,end="")  # puri line stars ki bana do
    else:                          # agar beech ki row ho
        print("*",end="")          # pehle ek star print karo
        print(" "*(n-2),end="")    # phir (n-2) spaces print karo 
        print("*",end="")          # last me ek star print karo
    print("")             # ek row complete hone ke baad new line

