"""
sum(1)=1
sum(2)=2+sum(1)
sum(3)=3+sum(2)
sum(n)=n+sum(n-1)

"""
def sum(n):
    if (n==1):
        return 1
    else:
        result=(n+sum(n-1))
        return result
n=int(input("Enter Number : "))
result=sum(n)
print(f"Sum is {result}")
   