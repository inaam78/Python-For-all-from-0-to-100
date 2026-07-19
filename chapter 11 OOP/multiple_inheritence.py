class Employee:
    company = "Google"
    language = "Python"
    def show(self):
        print(f"company name is {self.company} and language they mostly work with is {self.language}")
class product_manager:
    Manager ="default Manager"
    def show_manager(self):
        print(f"Product manager name is {self.Manager} ")

class Programmer(Employee,product_manager):
    language = "Python"
    name = "default name"
    def show_language(self):
        print(f"Programmer {self.name} knows {self.language}")

b=Programmer()
b.show() # Employee class ka show method call hoga kyunki wo pehle hai
b.show_manager() # product_manager class ka show_manager method call hoga
b.show_language() # Programmer class ka show_language method call hoga
# ye sary program me object b ke through call ho rhe hain ,agar hum Employee class ka show method call krte to bhi same output aata kyunki wo method Programmer class me inherit ho chuka hai