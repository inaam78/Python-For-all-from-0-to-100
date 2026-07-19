'''Walrus Operator (:=) Python Mein

Walrus Operator Python 3.8 mein introduce hua tha.

Iska kaam hai:

Variable ko value assign bhi karo aur usi waqt use bhi karo.

Normal Tarika
name = input("Enter your name: ")

if name:
    print(name)

Pehle value assign ki, phir use ki.

Walrus Operator Wala Tarika
if (name := input("Enter your name: ")):
    print(name)

Yahan:

name := input(...)

ka matlab:

Input lo
name mein save karo
Usi value ko if mein check bhi karo

Ek hi line mein dono kaam ho gaye.

Example 2

Without Walrus:

numbers = [1, 2, 3, 4]

length = len(numbers)

if length > 3:
    print(length)

With Walrus:

numbers = [1, 2, 3, 4]

if (length := len(numbers)) > 3:
    print(length)

Output:

4
Example 3 (Loop)
while (data := input("Enter something: ")) != "quit":
    print("You entered:", data)

Run:

Enter something: Ali
You entered: Ali

Enter something: Khan
You entered: Khan

Enter something: quit

Loop stop ho jayega.

Difference Between = and :=
Assignment Operator
x = 10

Sirf value assign karta hai.

Walrus Operator
print(x := 10)

Output:

10

Yahan assign bhi hua aur value return bhi hui.

Tumhare Number Guessing Game Mein

Walrus operator use kar sakte ho:

import random

secret = random.randint(1, 100)
attempts = 0

while (guess := int(input("Guess Number: "))) != secret:
    
    attempts += 1

    if guess < secret:
        print("Guess Higher Number")

    else:
        print("Guess Lower Number")

print(f"Correct! Attempts = {attempts + 1}")
Viva Mein Kya Kehna Hai?

Short Answer:

Walrus Operator (:=) allows assignment and expression evaluation in a single statement. It reduces code repetition and is useful in conditions and loops.

Dosto Wali Language

Socho tumhe pehle value save karni hai aur phir foran use bhi karni hai.

Normal:

name = input()
print(name)

Walrus:

print(name := input())

Ek hi line mein save bhi ho gaya aur print bhi ho gaya.

Isi shortcut ko Walrus Operator (:=) kehte hain.
 🦭 (Iska naam walrus isliye rakha gaya kyunki := walrus ke face jaisa lagta hai.'''