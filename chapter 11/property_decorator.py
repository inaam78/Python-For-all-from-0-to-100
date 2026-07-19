class employee:
    a=1
    @classmethod
    def show(self):
        print(f"employee class ka constructor{self.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter 
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

o=employee()
o.a=10
o.name="ali khan"
print(o.name)
o.show()