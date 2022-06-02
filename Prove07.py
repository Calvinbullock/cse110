#

from wsgiref.util import guess_scheme


print("Welcome to the word guessing game!")
a_b_c = input("Do you want to guess word A, B, or C? ").upper()

if a_b_c == "A":
    secret_word = "hello"
elif a_b_c == "B":
    secret_word = "red"
elif a_b_c == "C":
    secret_word = "computer"

guess = input("What is your guess? ").lower()
i = 0
extra = ""
e = 1

# removes the extra length from the longer word and saves it to extra
if len(secret_word) > len(guess):
    e = len(secret_word) - len(guess)
    while e < len(secret_word): 
        extra = extra + secret_word[e]

        while i < e:
            short_word = secret_word[i]

elif len(secret_word) < len(guess):
    e = len(guess) - len(secret_word)
    while e < len(guess): 
        extra = extra + guess[e]

    while i < e:
        short_word = guess[i]

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

    print(f"Your hint is: {answer + extra}")
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