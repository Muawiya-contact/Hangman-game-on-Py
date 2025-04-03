# Hangman Game

## Description
A text-based Hangman game written in Python. The program selects a random word, and the player guesses one letter at a time to uncover the word. The game allows a limited number of incorrect guesses before the player loses.

## Features
- Random word selection.
- Tracks guessed letters.
- Limits incorrect attempts to 6.
- Displays the current progress of the word.
- Provides user-friendly messages.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Muawiya-contact/hangman-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```
3. Run the game:
   ```bash
   python hangman.py
   ```

## Usage
1. The game will display an underscore `_` for each letter in the hidden word.
2. The player enters a single letter guess.
3. If the letter is correct, it is revealed in the word.
4. If the letter is incorrect, the number of attempts decreases.
5. The game continues until the word is guessed or the player runs out of attempts.

## Example Output
```
Welcome to Hangman! Test your word-guessing skills.

Current Word:  _ _ _ _ _ _
Attempts Remaining: 6
Enter a letter: p

Excellent! The letter is part of the word.

Current Word:  p _ _ _ _ _
Attempts Remaining: 6
Enter a letter: x

Incorrect guess. Please try again.

Current Word:  p _ _ _ _ _
Attempts Remaining: 5
...
```

## Contact Me
Gmail:contacmuawia@gmail.com
GitHub: https://github.com/Muawiya-contact

