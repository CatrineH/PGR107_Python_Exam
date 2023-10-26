"""
                                                                                            Candidatenr: 1017
Note!

I have chosen not to comment the code explicitly,
but instead I have converted "comments" to variables, methods and class names to make the code self-explanatory.
I have also used a visual separator or divider to improve the readability and organization of the output.
Maybe this isn't the best way to practice. But in this case I find it easier to check/control the code 
and understand it this way.

"""

import random

def read_words(word_guessing):
    with open(word_guessing, "r") as file:
        words = file.read().split()
    return words

def choose_letter():
    guessed_letters = ("a", "b", "c", "d", "e", "f", "g", "h",
                       "i", "j", "k", "l", "m", "n", "o", "p",
                       "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

    return random.choice(guessed_letters)

def play_game(word):
    guessed_letters = ["_"] * len(word)
    wrong_guesses = 0
    print("---------------------------------------------------------")
    print(f"\nTHE WORD YOU NEED TO GUESS HAS {len(word)} CHARACTERS.\n")
    print(f"You have {max_wrong_guesses} guesses.\n")
    print("---------------------------------------------------------")
    while wrong_guesses < max_wrong_guesses and "_" in guessed_letters:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_letters[i] = guess
            print(" ".join(guessed_letters))
        else:
            wrong_guesses += 1
            print("---------------------------------------------------------")
            print("Sorry, that letter is not in the word.")
            print(" ".join(guessed_letters))

    if "_" not in guessed_letters:
        print("---------------------------------------------------------")
        print(f"Congratulations! You guessed the word '{word}'!")
    else:
        print("---------------------------------------------------------")
        print(f"Sorry, you lost. The word was '{word}'.")
        print("---------------------------------------------------------")
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        print("---------------------------------------------------------")
        print(f"Number of wrong guesses: {wrong_guesses}")

words = read_words("word_guessing.txt")

while True:
    target_word = random.choice(words)
    if len(target_word) <= 8:
        max_wrong_guesses = len(target_word)
    else:
        max_wrong_guesses = len(target_word) + 2
        
    play_game(target_word)
    print("---------------------------------------------------------")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
print("---------------------------------------------------------")
print("Thanks for playing guessing game!")
print("---------------------------------------------------------")