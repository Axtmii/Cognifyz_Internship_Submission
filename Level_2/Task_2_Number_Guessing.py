import random

number = random.randint(1, 50)

print("Guess the number between 1 and 50.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        break