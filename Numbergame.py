# Guess the Number Game

import random
print("Guess the number between 1 and 100!")
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number:"))
    if guess < number:
        print("To Low Number!")
    elif guess > number:
        print("To High Number!")
    else:
        print("Congratulations You Got Is Right!")
        break 
        