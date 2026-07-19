class twodvector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"the value of x is {self.x} and the value of y is {self.y}")    
class threedvector():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def show(self):
        print(f"the value of x is {self.x}, y is {self.y}, and z is {self.z}")
v1=twodvector(10,20)
v2=threedvector(10,20,30)
v1.show()
v2.show()