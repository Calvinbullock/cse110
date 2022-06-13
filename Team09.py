num_list = []
new_num = 1

print("Enter a list of numbers, type 0 when finished.")
while new_num != 0:
    new_num = int(input("Enter number: "))

    if new_num != 0:
        num_list.append(new_num)

# This code block determains the sum of num_list
sum = 0
for i in num_list: 
    sum += i

print(f"The sum is: {sum}")
