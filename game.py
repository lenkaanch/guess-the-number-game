import random

secret_number = random.randint(1, 10)
print("Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 10.")
guess = input("Enter your guess: ")
if int(guess) == secret_number:
    print("Correct! You guessed the number.")
else:
    print("Wrong guess.")
