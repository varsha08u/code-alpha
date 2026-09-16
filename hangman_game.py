import random

WORDS = ["python", "computer", "programming", "developer", "algorithm"]
MAX_WRONG_GUESSES = 6


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n=== HANGMAN GAME ===")
    print("Guess the word one letter at a time.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Wrong guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses}")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            return

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Wrong guess.")

    print("\nGame over! The word was:", word)


if __name__ == "__main__":
    play_hangman()
