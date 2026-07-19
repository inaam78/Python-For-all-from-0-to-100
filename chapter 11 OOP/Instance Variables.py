'''Instance Variables

Different for every object.'''

class Student:

    def __init__(self,name):
        self.name = name

s1 = Student("Ali")
s2 = Student("Ahmed")

print(s1.name)
print(s2.name)