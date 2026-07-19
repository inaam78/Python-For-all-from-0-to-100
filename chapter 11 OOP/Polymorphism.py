'''Polymorphism

One interface, many forms.

Method Overriding'''
class Animal:

    def sound(self):
        print("Animal")

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()

'''Output
Bark'''


# Duck Typing
class Duck:

    def speak(self):
        print("Quack")

class Person:

    def speak(self):
        print("Hello")

def call(obj):
    obj.speak()

call(Duck())
call(Person())
'''Operator Overloading'''
class Number:

    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return self.value + other.value

a = Number(10)
b = Number(20)

print(a+b)