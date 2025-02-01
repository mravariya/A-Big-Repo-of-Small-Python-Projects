import random

# declaring all the constant

NUM_DIGITS = 3
MAX_GUESSES = 10

welcome_message = """Welcome to Bagels: A Deductive Logic Game

Game Rules:
- You will make guesses, and the game will provide feedback in the form of one of the following clues:
  - "Bagels": No digits in your guess are correct.
  - "Pico": One digit in your guess is correct but in the wrong position.
  - "Fermi": One digit in your guess is correct and in the correct position.
- The goal is to guess the secret number by using these clues and logic to eliminate incorrect guesses.

Good luck, and may your deductive reasoning lead you to victory!"""

print(welcome_message)

def main():
    while True:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guess to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answers was {}.".format(secretNum))
        
        print("Do you want to play again? (yes or no)")

        if not input("> ").lower().startswith('y'):
            break
    print("Thanks for playing!")

