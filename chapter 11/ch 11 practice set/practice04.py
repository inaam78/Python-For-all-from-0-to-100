class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
c1=complex(1,2)
c2=complex(3,4)
c3=c1+c2
print(f"real part of c3 is {c3.r} and imaginary part of c3 is {c3.i}")