class Employee:
    language = "Python"
    salary = 50000
    def getinfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")
    def greet(self):
        print("Hello, welcome to the company!")
    def __init__(self):    
        print("Employee object created") 
     # this is constructor method which is automatically called when we create an object of class



emp1 = Employee()
print(emp1.language, emp1.salary)
emp2 = Employee()
emp2.name = "Inam" 
print(emp2.name, emp2.language, emp2.salary) 
emp1.getinfo()
emp1.greet()
emp2.getinfo()
