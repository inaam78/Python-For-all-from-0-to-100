# Instance Method
class Student:

    def greet(self):
        print("Welcome")

student = Student()

student.greet()
# Class Method

# Uses @classmethod.

class Student:

    school = "ABC"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
''' Static Method

Does not use self or cls.'''

class Calculator:

    @staticmethod
    def add(a,b):
        return a+b

print(Calculator.add(10,20))