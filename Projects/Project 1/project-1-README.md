### Bagels: A Deductive Logic Game

#### Project Description
Bagels is a fun deductive logic game where you must guess a secret three-digit number. The secret number is composed of three unique digits (e.g., 438, 205). Based on your guesses, the game provides feedback to help you narrow down the possible solutions.

#### Game Rules:
- You will make guesses, and the game will provide feedback in the form of one of the following clues:
  - **"Bagels"**: No digits in your guess are correct.
  - **"Pico"**: One digit in your guess is correct but in the wrong position.
  - **"Fermi"**: One digit in your guess is correct and in the correct position.
- The goal is to guess the secret number by using these clues and logic to eliminate incorrect guesses.

#### How to Play:
1. The program randomly generates a three-digit secret number.
2. You will input guesses (three-digit numbers) one at a time.
3. After each guess, the game will provide feedback in the form of one of the above clues ("Bagels", "Pico", or "Fermi").
4. Continue guessing until you correctly identify the secret number.

#### Instructions:
1. Clone or download this repository.
2. Run the Python script `bagels.py` to start the game.
3. Follow the on-screen prompts to make your guesses.
4. Use the clues provided to adjust your next guess and continue until you find the secret number.

#### Example:
- Secret number: `427`
- Your guess: `123`
  - Feedback: **"Pico"** (One correct digit, but in the wrong position)
- Your guess: `452`
  - Feedback: **"Fermi"** (One correct digit, in the correct position)
- Your guess: `427`
  - Feedback: **"You win!"** (You guessed the number correctly!)

Good luck, and may your deductive reasoning lead you to victory!