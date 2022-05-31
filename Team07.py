import random

play_again = "yes"

while play_again == "yes":
    num = random.randint(1,10) #18
    
    guess = int(input("What is your guess? ")) #20
    guess_num = 1

    while guess != num:
        if guess > num:
            print("Lower")
        elif guess < num:
            print("higher")
        guess = int(input("What is your guess? ")) #20
        guess_num = guess_num + 1

    print("You guessed it!")
    print(f"It took you {guess_num}")
    play_again = input("Do you want to play again? (Yes/No) ").lower()
