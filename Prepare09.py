
names = []
new_name = ""
i = 0

while new_name.upper() != "END":
    new_name = input("Type the name of a friend: ")

    if new_name.upper() != "END":
        names.append(new_name)
        i += 1

for i in names:
    print()
    print("Your friends are:")
    print(i)


