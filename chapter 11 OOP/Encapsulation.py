'''Encapsulation

Encapsulation hides data from direct access.

Public Variable'''
class Student:

    def __init__(self):
        self.name = "Ali"

student = Student()

print(student.name)
'''Protected Variable

Single underscore (_).'''

class Student:

    def __init__(self):
        self._name = "Ali"
'''Private Variable

Double underscore (__).'''

class Student:

    def __init__(self):
        self.__password = "1234"

student = Student()

print(student._Student__password)
'''Getter and Setter'''
class Student:

    def __init__(self):
        self.__age = 20

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

student = Student()

print(student.get_age())

student.set_age(25)

print(student.get_age())