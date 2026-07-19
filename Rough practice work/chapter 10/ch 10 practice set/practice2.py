# class calculator:
#     def add(self, a, b):
#         return a + b
#     def subtract(self, a, b):
#         return a - b
#     def multiply(self, a, b):
#         return a * b
#     def divide(self, a, b):
#         if b != 0:
#             return a / b
#     def square(self, a):
#         return a * a
#     def cube(self, a):
#         return a * a * a
#     def square_root(self, a):
#         return a ** 0.5
# calc = calculator()
# print(calc.add(5, 3))
# print(calc.subtract(5, 3))
# print(calc.multiply(5, 3))
# print(calc.divide(5, 3))
# print(calc.square(5))
# print(calc.cube(5))
# print(calc.square_root(25))

class calculator:
    def __init__(self,n):
        self.n=n
        def square(self):
            return self.n * self.n
        def cube(self):
            return self.n * self.n * self.n
        def square_root(self):
            return self.n ** 0.5
calc=calculator(5)
print(calc.square())
print(calc.cube())
print(calc.square_root())