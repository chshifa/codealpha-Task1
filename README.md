# codealpha-Task1
TASK 1: Hangman Game
import random
lst = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "mango","orange", "papaya", "quince", "raspberry", "strawberry", "vanilla", "watermelon"]
word = random.choice(lst)
guesses = []
choosen= []
correct = 0

def display_word():
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
incorrect_guesses = 0
def hangman():
    global incorrect_guesses
    while incorrect_guesses < 6:
        print(display_word())
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guesses:
            print("You already guessed that letter.")
            continue
        guesses.append(guess)
        if guess in word:
            print("Good guess!")
            if all(letter in guesses for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                return
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {6 - incorrect_guesses} attempts left.")
    print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
