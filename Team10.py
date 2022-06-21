


acounts = ["checking", "savings"]
balances = [238.12, 392.99]

# acounts = ["checking", "saveing", "e fund"]
# balances = [102.57, 82.32, 200.00]

# acounts = []
# balances = []

acount = ""
print("Enter the names and balances of bank accounts (type: quit when done).")

while acount.upper() != "QUIT":
    acount = input("What is the name of this account? ")

    if acount.upper() != "QUIT":
        balance = float(input("What is the balance? "))
        acounts.append(acount)
        balances.append(balance)

total = 0
highest = 0
print("Account Information:")

for i in range(len(balances)):
    print(f"{i}. {acounts[i]} - {balances[i]}")
    total += balances[i]
    highest = max(highest, balances[i])

average = total / len(balances)

print()
print(f"Total: ${total}")
print(f"Average: ${round(average, 2)}")
print(f"Highest balance: savings - ${highest}")

update = ""

while update.upper() != "NO":
    print()
    update = input("Do you want to update an account? ")

    if update.upper() == "YES":
        index = int(input("What account index do you want to update? "))
        amount = float(input("What is the new amount? "))

        balances[index] = amount

        for i in range(len(balances)):
            print(f"{i}. {acounts[i]} - {balances[i]}")

    




# TODO - Strech challanges ---- TODO
# Determine which bank account has the highest balance and display the name and balance of that account.

# Change your display so that it shows the index of the account next to the name.

# After displaying the list, ask the user if they want to update an account.
# If they respond with yes, ask for the index of the account, and the new balance.

# Change the last step into a loop, so that the user can keep updating accounts until they say no.
# After each update, display the new list of balances.

# Account Information:
# 0. checking - $238.12
# 1. savings - $392.99

# Total: $631.11
# Average: $315.56
# Highest balance: savings - $392.99

# Do you want to update an account? yes
# What account index do you want to update? 1
# What is the new amount? 425.50

# Account Information:
# 0. checking - $200.00
# 1. savings - $425.50

# Do you want to update an account? no

# Account Information:
# 0. checking - $200.00
# 1. savings - $425.50


# TODO - basic requierments ---- TODO
# Create two lists, one for the names of the bank accounts, and one for the balances.

# Ask the user for the name of the bank account and then for it's current balance.
# Keep looping until the user types "quit" for the name of an account.
# For each one, add the name and the balance to the appropriate list.

# Loop through the lists using an index and display the name of the account with the balance next to it.

# Compute and display the total balance in all of the accounts and the average balance.

# Enter the names and balances of bank accounts (type: quit when done)
# What is the name of this account? checking
# What is the balance? 102.57
# What is the name of this account? savings
# What is the balance? 82.32
# What is the name of this account? emergency fund
# What is the balance? 200.00
# What is the name of this account? quit

# Account Information:
# checking - $102.57
# savings - $82.32
# emergency fund - $200.0

# Total: $384.89
# Average: $128.30