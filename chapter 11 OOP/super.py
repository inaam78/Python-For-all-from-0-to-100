class employee:
    def __init__(self):
        print("employee class ka constructor")
    a=1
class  Manager(employee) :
        def __init__(self):
            print("Manager class ka constructor")
        b=2
class Programmer(Manager):
    def __init__(self):
        super().__init__() # super() function ka use karke parent class ka constructor call kar rahe hain
        print("Programmer class ka constructor")
    c=3
o=employee()
print(o.a) # employee class ka a attribute print hoga
o=Manager()
print(o.a,o.b) # Manager class ka b attribute print hoga
o=Programmer()
print(o.a,o.b,o.c) # Programmer class ka c attribute print hoga