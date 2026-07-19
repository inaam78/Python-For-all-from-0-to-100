class Employee:
    company = "Google"
    def show(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")
# class Programmer:
#     company = "Microsoft"
#     def show(self):
#         print(f"Programmer name is {self.name} and salary is {self.salary}")
#     def show_language(self):
#         print(f"Programmer {self.name} knows {self.language}")
# a= Employee()
# b= Programmer()
# print(a.company,b.company)
class Programmer(Employee):
    language = "Python"
    def show_language(self):
        print(f"Programmer {self.name} knows {self.language}")
# a=Employee()
# a.name="Ali"
# a.salary=50000
b=Programmer()
b.name="Ahmed"
b.salary=60000
b.language="Java"
# print(a.company,a.name,a.salary)
print(b.company,b.name,b.salary,b.language)