import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

print("I am thinking of a number between 1 and 10.")
guess = input("Enter your guess: ")
if int(guess) == secret_number:
    print("Correct! You guessed the number.")
else:
    print("Wrong guess.")
    print("The correct number was:", secret_number)

# Generate random number
# Ask player for input
# Check if the guess is correct
