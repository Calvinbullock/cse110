

from tokenize import Double


pos_num = int(input("Please type a positive number: ")) #-3

while pos_num < 0:
    print("Sorry, that is a negative number. Please try again.")
    pos_num = int(input("Please type a positive number: ")) #-3
print(f"The number is: {pos_num}")

get_candy = input("May I have a piece of candy? ").upper()
while get_candy == "NO":
    get_candy = input("May I have a piece of candy? ").upper()
print("Thank you.")