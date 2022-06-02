#

from pickle import FALSE
from re import A


secret_word = "Hello".lower()

print("Welcome to the word guessing game!")
guess = input("What is your guess? ").lower()
i = -1

while guess != secret_word:
    answer = ""

    while i < min(len(secret_word), len(guess)):
        i = i + 1

        if i < min(len(secret_word), len(guess)) and guess[i] == secret_word[i]: #in word at that location
            answer = answer + guess[i].upper()

        elif i < min(len(secret_word), len(guess)): #letter is in word anywhere
            letter = guess[i]
            j = 0
            letterInWord = True

            while j < len(guess):
                if letter == secret_word[j]:
                    answer = answer + guess[i].lower()
                    letterInWord = False

                j = j + 1

            if letterInWord: # if the letter is not in the secret word
                answer = answer + "_"

    print(f"Your hint is: {answer}")
    guess = input("What is your guess? ")
    
print("Congratulations! You guessed it!")

# TODO Rules
# An underscore _ indicates that the letter was not present in the secret word.
# A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.

# An uppercase letter indicates that the letter was present at that exact spot in the secret word. 
# (In other words, if the second letter in the guess is also the second letter in the secret word, 
# then that letter is shown as a capital.)




#TODO output ex 1

# Welcome to the word guessing game!

# What is your guess? temple
# Your guess was not correct.
# What is your guess? moroni
# Your guess was not correct.
# What is your guess? mosiah
# Congratulations! You guessed it!
# It took you 3 guesses.

#TODO output ex 1

# Your hint is: _ _ _ _ _ _ 
# What is your guess? temple
# Your hint is: _ _ m _ _ _ 
# What is your guess? moroni
# Your hint is: M O _ o _ i 
# What is your guess? hhhhhh
# Your hint is: h h h h h H 
# What is your guess? mosiah  
# Congratulations! You guessed it!
# It took you 4 guesses.