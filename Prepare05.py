

num_1 = int(input("What is the first number? "))
num_2 = int(input("What is the seconed number? "))
print()

# is the first num greater?
if num_1 > num_2:
    print("The first number is greater")
else:
    print("The first number is not greater")

# are the nums equal
if num_1 == num_2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

# is the second num greater?
if num_1 < num_2:
    print("The second number is greater")
else:
    print("The second number is not greater")

print()

# Is my and there favorite the same?
animal = input("What is your favorite animal? ").capitalize()
if animal == "Fox":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")