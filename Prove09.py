

cart_items = []
item_prices = []
exit = True
total = 0

print("Welcome to the Shopping Cart Program!")
while exit:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = int(input("Please enter an action: "))

    # Add item
    if action == 1:
        item = input("What item would you like to add? ")
        cart_items.append(item)
        price = float(input(f"What is the price of '{item}'? "))
        item_prices.append(price)
        print(f"'{item}' has been added to the cart.")

    # View cart
    elif action == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(cart_items)):
            print(f"{i+1}. {cart_items[i]} - ${round(item_prices[i], 2)}")

    # Remove item
    elif action == 3:
        # Will prin the contents of the cart
        print("The contents of the shopping cart are:")
        for i in range(len(cart_items)):
            print(f"{i+1}. {cart_items[i]} - ${round(item_prices[i], 2)}")

        print()
        remove_item = int(input("Which item would you like to remove? "))
        remove_item -= 1 

        # The index they used is not in the list range
        if remove_item > len(cart_items)-1 or remove_item < 0:
            print("sorry, that is not a valid item number.")

        # All good remove item
        elif remove_item >= 0:
            removed = cart_items.pop(remove_item)
            item_prices.pop(remove_item)
            print(f"Item removed was {removed}.")

        else:
            print("Number was not an item.")

    # Compute total
    elif action == 4:
        total = 0
        for i in item_prices:
            total += i

        print(f"The total price of the items in the shopping cart is ${round(total, 2)}")

    # Quit
    elif action == 5:
        exit = False
        print("Thank you. Goodbye.")

    print()



# TODO need to add a creativity thing
# It will print out the cart when ever you ask to delete an item


## Have menu system that repeats until the user chooses quit.

## Create a list that will store the names of the items in the shopping cart.

## Complete the option to add the name of the item to the list.

## Complete the option to display the names of the items in the list.

# TODO Final req (below)

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