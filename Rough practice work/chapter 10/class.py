class Employee:
    language = "Python"
    salary = 50000
emp1 = Employee()
print(emp1.language, emp1.salary)
emp2 = Employee()
emp2.name = "Inam" # this is object attribute because it belongs to object not class
print(emp2.name, emp2.language, emp2.salary) 
# As their name is object attribute and langauage and salary are class attributes 
# ,because they directly belongs to class.
 
