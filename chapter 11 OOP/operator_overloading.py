class number:
    a=1
    b=2
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return self.n+other.n
o1=number(10)
o2=number(20)
print(o1+o2)