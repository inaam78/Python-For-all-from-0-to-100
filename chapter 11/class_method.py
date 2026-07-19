class employee:
    a=1
    @classmethod
    def show(self):
        print(f"employee class ka constructor{self.a}")
o=employee()
o.a=10
o.show()