#

from ctypes.wintypes import WORD
from re import I
from turtle import position


secret_word = "Hello"

print("Welcome to the word guessing game!")
guess = input("What is your guess? ")

i = 0
while guess.upper() == secret_word.upper():
    print("Your guess was not correct.")
    guess = input("What is your guess? ")

    letter = guess[i]
    j = 0
    i =+ 1
    answer = ""
    while j < len(guess):
        j =+ 1
        if secret_word[j] == letter:
            answer = secret_word[j]
        elif 


if letter not in WORD
    + "_"
elif letter is in word
    + letter.lower()
elif letter == secret_word[j]
    answer + letter.upper()
        
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