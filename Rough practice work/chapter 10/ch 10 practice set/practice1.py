class Employee:
    def __init__(self, name, salary,age,department,position):
        self.name = name
        self.salary = salary
        self.age = age
        self.department = department
        self.position = position
    def getinfo(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Age: {self.age}, Department: {self.department}, Position: {self.position}")
emp1 = Employee("Inam", 50000, 30, "IT", "Software Engineer")
emp1.getinfo()
emp2 = Employee("Ali", 60000, 35, "HR", "HR Manager")
emp2.getinfo()