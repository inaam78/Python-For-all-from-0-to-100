def factorial(n):
 if (n==1):
  return 1
 else:
   return (n*factorial(n-1))
n=int(input("Enter Number : "))
result=factorial(n)
print(f"Factorial is {result}")
# how the function works for factorial(5):
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1 * factorial(0)
# = 5 * 4 * 3 * 2 * 1 * 1
# = 120