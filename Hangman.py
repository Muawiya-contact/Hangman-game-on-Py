import random

def choose_word():
    """
    Selects a random word from a predefined list.
    """
    words = ['python', 'programming', 'hangman', 'developer', 'computer', 'science','codealpha','codingmoves']
    return random.choice(words)

def display_word(word: str, guessed_letters: set) -> str:
    """
    Returns the word with guessed letters revealed and unguessed letters replaced with underscores.
    """
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    """
    Implements the Hangman game logic, allowing a player to guess letters of a randomly chosen word
    within a limited number of incorrect attempts.
    """
    word = choose_word()
    guessed_letters = set()
    max_attempts = 6
    attempts_remaining = max_attempts

    print("Welcome to Hangman! Test your word-guessing skills.")
    
    while attempts_remaining > 0:
        print("\nCurrent Word: ", display_word(word, guessed_letters))
        print(f"Attempts Remaining: {attempts_remaining}")
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You have already guessed this letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Excellent! The letter is part of the word.")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You have successfully guessed the word:", word)
                break
        else:
            attempts_remaining -= 1
            print("Incorrect guess. Please try again.")
    else:
        print("\nGame Over. The correct word was:", word)

if __name__ == "__main__":
    hangman()

#By Coding Moves
