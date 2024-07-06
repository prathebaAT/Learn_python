import random
from words import words
from visuals import display_hangman


def get_random_word():
    return random.choice(words)

def play_hangman():
    word_to_guess = get_random_word()
    word_display = "_" * len(word_to_guess)
    guessed_letters = []
    tries = 6
    print("Welcome to Hangman!")
    
    while tries > 0 and "_" in word_display:
        print(display_hangman(tries))
        print("Word to guess: ", " ".join(word_display))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            word_display = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess]) #list comprehension
        else:
            guessed_letters.append(guess)
            tries -= 1
            print(f"Incorrect! You have {tries} tries left.")
        
    if "_" not in word_display:
        print(f"Congratulations! You guessed the word: {word_to_guess}")
    else:
        print(display_hangman(tries))
        print(f"Game over! The word was: {word_to_guess}")

play_hangman()