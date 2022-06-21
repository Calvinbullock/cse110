shopping_list = []
new_name = ""
i = 0

while new_name.upper() != "END":
    new_name = input("Type the name of a friend: ")

    if new_name.upper() != "END":
        shopping_list.append(new_name)
        i += 1

for i in range(len(shopping_list)):
    print()
    print(f"{i}. {shopping_list[i]}")
    print(i)


# Verify that you can add all the items to the list and display them. 
# (Verify similar to the check point from the previous lesson.)

# Iterate through the list using an index. 
# Verify that your program displays the index before the item and that the index starts at 0 
# for the first item.

# Verify that you can ask the user to type an index and a new item.

# Set the value at that index to be the new item the user typed. Verify that this does not cause errors.

# Print the items out again, and verify that your new item is in the list at the correct spot.