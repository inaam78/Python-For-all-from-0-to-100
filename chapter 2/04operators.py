#Arithmetic operators
a = 10
b = 20
print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print(a % b) #modulus
print(a ** b) #exponentiation
print(a // b) #floor division


#Assignment operators
a = 10
b = 20

b += 3
print (b) #b = b + 3 increment the value of b by 3 and then assign into b

b -= 3
print (b) #b = b - 3 decrement the value of b by 3 and then assign into b

a += b #a = a + b increment the value of a by b and then assign into a
print(a)

a -= b #a = a - b decrement the value of a by b and then assign into a
print(a)

a *= b #a = a * b multiply the value of a by b and then assign into a
print(a)

a /= b #a = a / b divide the value of a by b and then assign into a
print(a)

a %= b #a = a % b modulus of a by b and then assign into a
print(a)

a **= b #a = a ** b exponentiation of a by b and then assign into a
print(a)

a //= b #a = a // b floor division of a by b and then assign into a
print(a)


#camparison operators
a = 10
b = 20
print(a == b) #comparison operators always give result in the form of boolean so its result is false
print(a != b) # a is not equal to b so it will give true
print(a > b) #a is greater than b so it will give false
print(a < b) #a is less than b so it will give true
print(a >= b) #a is greater than or equal to b so it will give false
print(a <= b) #a is less than or equal to b so it will give true


#Logical operators
e = True or False
# Truthtable of or
# A     B     A or B
# True  True  True
# True  False True
# False True  True
# False False False
print(e) #True

f = True and False
# Truthtable of and
# A     B     A and B
# True  True  True
# True  False False
# False True  False
# False False False
print(f) #False

g = not True
# Truthtable of not
# A     not A
# True  False
# False True
print(g) #False
