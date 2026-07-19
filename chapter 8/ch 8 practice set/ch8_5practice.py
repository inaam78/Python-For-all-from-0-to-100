#using loops
# def pattern(n):
#     for i in range(n-1, -1, -1):
#         for j in range(i + 1):
#             print("*", end="")
#         print()
# n = int(input("Enter the number of rows: "))

# pattern(n)

#using recursion

def pattern(n):
  if n == 0:
    return
  print("*"*n)
  pattern(n-1)
n = int(input("Enter the number of rows: "))
pattern(n)

"""
🔹 Step by Step Execution (Suppose n = 5)

pattern(5)

print "*****"

call pattern(4)

pattern(4)

print "****"

call pattern(3)

pattern(3)

print "***"

call pattern(2)

pattern(2)

print "**"

call pattern(1)

pattern(1)

print "*"

call pattern(0)

pattern(0)

yahan if n == 0: return lag gaya

matlab aur call nahi hogi → recursion ruk gaya ✅
"""