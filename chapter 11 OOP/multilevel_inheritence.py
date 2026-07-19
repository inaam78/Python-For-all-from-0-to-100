class employee:
   a=1
class  Manager(employee) :
    b=2
class Programmer(Manager):
    c=3
o=employee()
print(o.a) # employee class ka a attribute print hoga
o=Manager()
print(o.a,o.b) # Manager class ka b attribute print hoga
o=Programmer()
print(o.a,o.b,o.c) # Programmer class ka c attribute print hoga