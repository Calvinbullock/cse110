# Author Calvin Bullock
# Date: 3rd of May 2022
# the green coments after the inputs are test inputs that will match the ouputs listed after the prints

# child_meal = float(input("What is the price of a child's meal? ")) #4.50 / 2.25
# adult_meal = float(input("What is the price of an adult's meal? ")) #9.00 / 6.99
# children = int(input("How many children are there? ")) #4 / 2
# adults = int(input("How many adults are there? ")) #2 / 1
# tax = float(input("What is the sales tax rate? ")) #6 / 4

# hard variables for quick testing
child_meal =  4.50 # 2.25
adult_meal = 9.00 # 6.99
children =  4 # 2
adults =  2 # 1
tax =  6 # 4

sub_total = (child_meal * children + adult_meal * adults)
tax = sub_total * (tax/100)
total = float( sub_total + tax)

print(f"\nSubtotal: ${sub_total:.2f}") #36.00 / 11.49
print(f"Sales Tax: ${tax:.2f}") #2.16 / 0.46
print(f"Total: ${total:.2f}\n") #38.16 / 11.95

payment = float(input("What is the payment amount? ")) #40 / 20
change = round(float(payment - total), 2)

# Checks that the payment is enough to meet total cost.
while change < 0:
    print("Your payment was to small, please make a full payment.")
    payment = float(input("What is the payment amount? ")) #40 / 20
    change = float(payment - total)

print(f"Change: ${change:.2f}") #$1.84 / 8.05