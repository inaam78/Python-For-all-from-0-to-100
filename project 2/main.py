# import random

# # Random number generate karega 1 se 100 ke darmiyan
# secret_number = random.randint(1, 100)

# attempts = 0

# while True:
#     guess = int(input("Guess the number (1-100): "))
    
#     attempts += 1

#     if guess < secret_number:
#         print("Guess Higher Number Please!")
    
#     elif guess > secret_number:
#         print("Guess Lower Number Please!")
    
#     else:
#         print(f"Congratulations! You guessed the number in {attempts} attempts.")
#         break

import random

# Random number generate karega 1 se 100 ke darmiyan
secret_number = random.randint(1, 100)

a =-1
guesses=0

while (a != secret_number):
    a= int(input("Guess the number (1-100): "))
    
    guesses += 1

    if a < secret_number:
        print("Guess Higher Number Please!")
    
    elif a > secret_number:
        print("Guess Lower Number Please!")
    
    else:
        print(f"Congratulations! You guessed the number{secret_number} in {guesses} attempts.")
    
    