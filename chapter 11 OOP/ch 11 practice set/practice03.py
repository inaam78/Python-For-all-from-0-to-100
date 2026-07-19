class employee:
    salary=210
    bonus=25
@property
def bonus(self):      
    return self.salary*0.25
@bonus.setter
def bonus(self,value):
    self.salary=value/0.25
o=employee()
o.bonus=25
print(o.bonus)
print(o.salary)