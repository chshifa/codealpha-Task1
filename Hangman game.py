# '''TASK 1: Hangman Game 
# Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time. 
# Simplified Scope: 
# ● Use a small list of 5 predefined words (no need to use a file or API). 
# ● Limit incorrect guesses to 6. 
# ● Basic console input/output — no graphics or audio. 
# Key Concepts Used: random, while loop, if-else, strings, lists. '''



# import random
# lst = ["apple", "banana", "cherry", "grape", "lemon", "mango","orange", "papaya", "raspberry", "strawberry", "vanilla", "watermelon"]
# word = random.choice(lst)
# guesses = []
# choosen= []
# correct = 0

# def display_word():
#     display = ""
#     for letter in word:
#         if letter in guesses:
#             display += letter + " "
#         else:
#             display += "_ "
#     return display.strip()
# incorrect_guesses = 0
# def hangman():
#     global incorrect_guesses
#     while incorrect_guesses < 6:
#         print(display_word())
#         guess = input("Guess a letter: ").lower()
#         if len(guess) != 1 or not guess.isalpha():
#             print("Please enter a single letter.")
#             continue
#         if guess in guesses:
#             print("You already guessed that letter.")
#             continue
#         guesses.append(guess)
#         if guess in word:
#             print("Good guess!")
#             if all(letter in guesses for letter in word):
#                 print(f"Congratulations! You've guessed the word: {word}")
#                 return
#         else:
#             incorrect_guesses += 1
#             print(f"Incorrect guess. You have {6 - incorrect_guesses} attempts left.")
#     print(f"Game over! The word was: {word}")

# if __name__ == "__main__":
#     hangman()
#     replay = input("Do you want to play again:(Yes/No) ").lower()

#     if replay == "yes":
#         hangman()
#     elif replay == "no":
#         print("Thanks for playing game")
#     else:
#         print("Sorry I don't understand ")


import random

WORDS = ["apple", "banana", "cherry", "grape", "lemon", "mango","orange", "papaya", "raspberry", "strawberry", "vanilla", "watermelon"]  # small list of 5 words
MAX_INCORRECT = 6

def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_game():
    word = random.choice(WORDS)
    guesses = set()
    incorrect = 0

    while incorrect < MAX_INCORRECT:
        print("\nWord:", display_word(word, guesses))
        # Show guessed letters so far
        if guesses:
            print("Guessed letters:", " ".join(sorted(guesses)))
        else:
            print("Guessed letters: None")

        # Ask the player for a guess
        guess = input("Guess a letter: ").lower().strip()


        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses.add(guess)

        if guess in word:
            print("Good guess!")
            if all(ch in guesses for ch in word):
                print(f"Congratulations! You've guessed the word: {word}")
                return
        else:
            incorrect += 1
            print(f"Incorrect guess. Attempts left: {MAX_INCORRECT - incorrect}")

    print(f"Game over! The word was: {word}")

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if replay in ("yes", "y"):
            continue
        elif replay in ("no", "n"):
            print("Thanks for playing!")
            break
        else:
            print("Sorry, I don't understand. Exiting. Thanks for playing!")
            break

if __name__ == "__main__":
    main()
