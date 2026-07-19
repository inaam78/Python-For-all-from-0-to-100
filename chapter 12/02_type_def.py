'''
Agar tum Python mein Type Definition (Type Hints) ki baat kar rahe ho, to ye Python ko batane ke liye use hota hai ke variable ya function kis type ka data expect karta hai.

Without Type Hint
name = "Ali"
age = 22

Python khud samajh leta hai types.

With Type Hint
name: str = "Ali"
age: int = 22
cgpa: float = 3.5

Yahan:

str = string
int = integer
float = decimal number
Function Type Hint

Without type hints:

def add(a, b):
    return a + b

With type hints:

def add(a: int, b: int) -> int:
    return a + b

Matlab:

a = int
b = int
return = int

Example:

result = add(5, 3)
print(result)

Output:

8
List Type
numbers: list[int] = [1, 2, 3, 4]

String list:

names: list[str] = ["Ali", "Ahmed"]
Dictionary Type
student: dict[str, int] = {
    "Ali": 90,
    "Ahmed": 85
}
Custom Class Type
class Employee:
    pass

emp: Employee = Employee()
Why Use Type Hints?

Benefits:

Code zyada readable hota hai.
IDE (VS Code, PyCharm) errors jaldi batati hain.
Large projects mein debugging easy ho jati hai.
Type Definition vs type()

Log aksar confuse hote hain.

type()

Type check karta hai:

x = 10

print(type(x))

Output:

<class 'int'>
Type Hint

Type batata hai:

x: int = 10

Ye check nahi karta, sirf hint deta hai.

Viva Answer

Type hints (type definitions) Python mein variables aur function parameters ke expected
 data types specify karne ke liye use hote hain. Ye code readability aur debugging improve
 karte hain.

Dosto Wali Language

Socho tum function likh rahe ho:

def add(a, b):

Kisi ko nahi pata a aur b kya honge.

Agar likh do:

def add(a: int, b: int) -> int:

To foran samajh aa jata hai:

Bhai ye function do integers lega aur integer return karega.

Isi ko Type Definition / Type Hinting kehte hain.

'''