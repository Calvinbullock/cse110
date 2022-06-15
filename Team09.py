
num_list = []
new_num = 1

print("Enter a list of numbers, type 0 when finished.")

while new_num != 0:
    new_num = int(input("Enter number: "))

    if new_num != 0:
        num_list.append(new_num)

num_list.sort()

# This code block determains the sum of num_list
sum = 0
for i in num_list: 
    sum += i

avrage = sum / len(num_list)

# This code block determains the largest number in num_list
max_num = 0
for i in num_list: 
    max_num = max(max_num, i)

# This code block determains the positive number closest to 0 in num_list
min_pos = 1000000 # Most numbers should be smaller then this
for i in num_list: 
    if i >= 0:
        min_pos = min(min_pos, i)


print(f"The sum is: {sum}")
print(f"The average is: {avrage}")
print(f"The largest number is: {max_num}")
print(f"The smallest positive number is: {min_pos}")
print(f"The sorted list is:")
for i in num_list: 
   print(i)