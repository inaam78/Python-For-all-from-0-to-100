'''Abstraction

Hide implementation details.'''

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side*self.side

square = Square(5)

print(square.area())
# Magic (Dunder) Methods
str()
class Student:

    def __str__(self):
        return "Student Object"

student = Student()

print(student)
len()
class Team:

    def __len__(self):
        return 5

team = Team()

print(len(team))
eq()
class Student:

    def __init__(self,age):
        self.age = age

    def __eq__(self,other):
        return self.age == other.age

a = Student(20)
b = Student(20)

print(a==b)
'''Property Decorator'''
class Student:

    def __init__(self):
        self.__age = 20

    @property
    def age(self):
        return self.__age

student = Student()

print(student.age)
'''Composition

A class contains another class.'''

class Engine:

    def start(self):
        print("Engine Started")

class Car:

    def __init__(self):
        self.engine = Engine()

car = Car()

car.engine.start()
'''Aggregation

One object uses another object, but both can exist independently.'''

class Teacher:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, teacher):
        self.teacher = teacher

teacher = Teacher("Mr. Khan")
department = Department(teacher)

print(department.teacher.name)
'''Destructor

Called when an object is destroyed.'''

class Student:

    def __del__(self):
        print("Object Deleted")

student = Student()

del student
'''Method Resolution Order (MRO)
Determines the order in which Python searches parent classes.'''

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())