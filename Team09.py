num_list = []
new_num = 1

print("Enter a list of numbers, type 0 when finished.")
while new_num != 0:
    new_num = int(input("Enter number: "))

    if new_num != 0:
        num_list.append(new_num)
