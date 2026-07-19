# a={"inaam":1111, "d": 222,"f":22,"list":[1,2,4]}
# print(a["list"])

# list=["usman","ali","hamza"]
# a=input("enter a name : ")
# if(a in list):
#    print("present")
# else:
#    print("not present")
# l=["ali","ahmed","hassan","hussain",1,False,2.5]
# i=0
# while(i<len(l)):
#     print(l(i))
#     i+=1
# a="text"
# if (a=="words" or a=="alphabet"):
#     print("letters")
# else:
#     print("numbers")
# def avg():
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     c=int(input("Enter third number: "))
#     average=(a+b+c)/3
#     print("The average of three numbers is: ",average)
#     return avg
# avg()
# a=avg()

# def greet(name):
#     match name:
#         case "Alice":
#             return "Hello, Alice!"
#         case "Bob":
#             return "Hi, Bob!"
#         case _:
#             return "Hello, Stranger!"        
# print(greet("Alice"))
# print(greet("Bob"))
# print(greet("Charlie"))

# fruits = ["Apple", "Banana", "Mango"]

# for index ,value in enumerate(fruits):
#     print(index, value)


# names = ["Ali", "Ahmed", "Usman"]

# lengths = [len(i) for i in names]

# print(lengths)

# numbers = [1,2,3,4,5]

# result = ["Even" if x%2==0 else "Odd" for x in numbers]

# print(result)

numbers = [1,2,3,4,5]

for i in range(0,5):
    if numbers[i] % 2 == 0:
        print("Even")
    else:
        print("Odd")
