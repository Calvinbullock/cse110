
cart_items = []
item_prices = []
exit = True

print("Welcome to the Shopping Cart Program!")
while exit:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = int(input("Please enter an action: "))

    if action == 1: # Add item
        item = input("What item would you like to add? ")
        cart_items.append(item)
        price = float(input(f"What is the price of '{item}'? "))
        item_prices.append(price)
        print(f"'{item}' has been added to the cart.")

    elif action == 2: # View cart
        print("The contents of the shopping cart are:")
        for i in range(len(cart_items)):
            print(f"{i+1}. {cart_items[i]} - ${round(item_prices[i], 2)}")

    elif action == 3: # Remove item
        remove_item = int(input("Which item would you like to remove? "))
        remove_item -= 1 

        if remove_item >= 0:
            del cart_items[remove_item]
            del item_prices[remove_item]
            print("Item removed.")

        else:
            print("Number was not an item.")

    elif action == 4: # Compute total
        total = 0
        for i in item_prices:
            total += i
        print(f"The total price of the items in the shopping cart is ${round(total, 2)}")

    elif action == 5: # Quit
        exit = False
        print("Thank you. Goodbye.")

    print()



## Have menu system that repeats until the user chooses quit.

## Create a list that will store the names of the items in the shopping cart.

## Complete the option to add the name of the item to the list.

## Complete the option to display the names of the items in the list.

# TODO Final req

## Store prices as well as names.

## Change the add functionality to also ask for and store the price of the item.

## Change the display functionality to also display the prices of the items.

## When displaying the items, display a number in front of each item. The numbers should start with 1.

## Complete the option to display the total amount of the prices of all the items in the shopping cart.

## Whenever prices are displayed, they should be shown to two decimal places.

## Complete the option to remove an item from the shopping cart.

# When removing an item, you should verify the following:

## Both the item name and price are removed from their respective lists.

# The number the user enters should be converted to a 0-based index and checked to make sure it is within the 
# bounds of the list.

# The program allows you to remove any item from the list including the first one and the last one. 
# (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)