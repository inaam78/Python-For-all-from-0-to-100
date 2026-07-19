# Here are some of the most commonly used string functions in Python, along with their purpose and implementation with examples:


# len(string):
# Purpose: Returns the number of characters in a string (its length).


text = "Hello"
length = len(text)
print(length)  # Output: 5


# lower():
# Purpose: Converts all characters in a string to lowercase.


text = "Hello World"
lower_text = text.lower()
print(lower_text)  # Output: hello world


# upper():
# Purpose: Converts all characters in a string to uppercase.


text = "Hello World"
upper_text = text.upper()
print(upper_text)  # Output: HELLO WORLD


# strip():
# Purpose: Removes leading and trailing whitespace (spaces, tabs, newlines) from a string.


text = "   Hello World   "
stripped_text = text.strip()
print(stripped_text)  # Output: Hello World


text = "***Hello***"
stripped_text = text.strip("*")
print(stripped_text) # Output: Hello


# replace(old, new):
# Purpose: Replaces all occurrences of a specified substring (old) with another substring (new).


text = "Hello World"
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Output: Hello Python


# split(separator):
# Purpose: Splits a string into a list of substrings based on a specified delimiter (separator). If no separator is provided, it defaults to whitespace.


text = "Hello,World,"
split_list = text.split(",")
print(split_list)  # Output: ['Hello', 'World', 'Python']


# join(iterable):
# Purpose: Concatenates elements of an iterable (like a list or tuple) into a single string, using the string on which the method is called as a separator.


words = ["Hello", "World", "Python"]
joined_string = " ".join(words)
print(joined_string)  # Output: Hello World Python

numbers = ("1", "2", "3")
joined_numbers = "-".join(numbers)
print(joined_numbers) # Output: 1-2-3


# find(substring):
# Purpose: Returns the index of the first occurrence of a specified substring within the string. If the substring is not found, it returns -1.   


text = "Hello World"
index = text.find("World")
print(index)  # Output: 6

index = text.find("Python")
print(index)  # Output: -1


# startswith(prefix):
# Purpose: Checks if the string starts with a specified prefix. Returns True if it does, and False otherwise.


text = "Hello World"
starts_with_hello = text.startswith("Hello")
print(starts_with_hello)  # Output: True

starts_with_hi = text.startswith("Hi")
print(starts_with_hi)  # Output: False


# endswith(suffix):
# Purpose: Checks if the string ends with a specified suffix. Returns True if it does, and False otherwise.


text = "Hello World"
ends_with_world = text.endswith("World")
print(ends_with_world)  # Output: True

ends_with_python = text.endswith("Python")
print(ends_with_python)  # Output: False


# count(substring):
# Purpose: Returns the number of non-overlapping occurrences of a substring in the string.


text = "Hello Hello World"
count_hello = text.count("Hello")
print(count_hello)  # Output: 2

count_o = text.count("o")
print(count_o) # Output: 3


# format():
# Purpose: Used for string formatting. It allows you to embed variables and expressions inside strings.

name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.   


# capitalize():

# Purpose: Returns a string with the first character converted to uppercase and the rest to lowercase.


text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text) # Output: Hello world


# title():
# Purpose: Returns a title-cased string where the first letter of each word is capitalized.


text = "hello world python"
title_text = text.title()
print(title_text) # Output: Hello World Python
