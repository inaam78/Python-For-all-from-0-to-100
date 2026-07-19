'''self Keyword

self refers to the current object.'''

class Student:

    def __init__(self,name):
        self.name = name

student = Student("Ali")

print(student.name)