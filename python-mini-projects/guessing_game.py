
import random

def guessing_game():
    number = random.randint(1, 100)
    tries = 0
    print("🎲 I'm thinking of a number between 1 and 100... Can you guess it?")

    while True:
        guess = int(input("Your guess: "))
        tries += 1

        if guess < number:
            print("Too low 📉")
        elif guess > number:
            print("Too high 📈")
        else:
            print(f"🎉 Correct! The number was {number}. You took {tries} tries.")
            break

guessing_game()
