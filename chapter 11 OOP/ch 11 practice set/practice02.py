class animals:
    def __init__(self,name):
        self.name=name

class pet(animals):
    def __init__(self,name,type):
        super().__init__(name)
        self.type=type

class dog(pet):
    def __init__(self,name,type,barking):
        super().__init__(name,type)
        self.barking=barking   
    def bark(self):
        print("woof woof")         
d1=dog("tommy","dog","loud")
print(d1.name)
print(d1.type)
print(d1.barking)
d1.bark()