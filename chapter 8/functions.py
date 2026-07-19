#defination of function
def avg():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    average=(a+b+c)/3
    print("The average of three numbers is: ",average)
def sum():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    total=a+b+c
    print("The sum of three numbers is: ",total)
def greet():
    name=input("Enter your name: ")
    print("Hello ",name)

def hello(name):
    print("hello,"+ name)

#calling function
avg()
sum()
greet()
hello("inam")