class Employee:
    language = "Python"
    salary = 50000
emp1 = Employee()
print(emp1.language, emp1.salary)
emp2 = Employee()
# emp2.language = "Java" instant attribiute got preference over class attribute 
print( emp2.language, emp2.salary) 