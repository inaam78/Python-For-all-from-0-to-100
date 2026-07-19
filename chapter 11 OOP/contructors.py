"""Constructor (init)

The constructor runs automatically whenever an object is created."""

class Student:

    def __init__(self):
        print("Constructor Called")

student = Student()

# Parameterized Constructor
class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

student = Student("Ali",20)

print(student.name)
print(student.age)