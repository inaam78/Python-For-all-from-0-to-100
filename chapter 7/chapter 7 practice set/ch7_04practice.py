"""
First check if n <= 1 → immediately say not prime.

Loop from 2 to n-1:

If n % i == 0 → number is divisible → not prime, exit loop.

If loop finishes without breaking → run the else → prime number."""
n = int(input("Enter your number: "))

if n <= 1:
    print("not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:       # only check divisibility
            print("not a prime number")
            break            # break only when a divisor is found
    else:
        print("prime number")
