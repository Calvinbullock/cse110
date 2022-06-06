


qoute = "in coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
cuntinue = "yes"

while "yes" == cuntinue:
    num = int(input("Please enter a number: "))
    
    for i in range(len(qoute)):
        if 0 == i%num:
            print(qoute[i].upper(), end="")
        else:
            print(qoute[i], end="")

    cuntinue = input("Would you like to enter another number(yes/no)? ").lower()


# word = "commitment"
# letter = input("What is your favorite letter? ").lower()

# for i in range(len(word)):
#     if letter == word[i]:
#         print("_", end="")
#     else:
#         print(word[i], end="")

print()