'''Inheritance

Inheritance allows one class to reuse another class.'''

class Animal:

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()

dog.speak()

'''Output

Animal speaks
Types of Inheritance
Single
A → B
Multiple
A
 \
  C
 /
B
Multilevel
A → B → C
Hierarchical
      A
    / | \
   B  C  D'''