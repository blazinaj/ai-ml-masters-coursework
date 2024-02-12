# ItemToPurchase Class from Module 4 Portfolio Milestone
class ItemToPurchase:

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    # Calculates the cost of the item based on price and quantity
    def calculate_cost(self):
        return self.item_price * self.item_quantity

    # Prints the item's name, quantity, price, and total cost
    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ " + "$" + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))


# Shopping Cart Class. Has a parameterized constructor, which takes the customer name and date as parameters.
# Includes methods for adding an item to cart_items list, removing item from cart_items list, modifying an item's description, price, and/or quantity,
class ShoppingCart:

    # Parameterized constructor, which takes the customer name and date as parameters
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price

                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity

                return

        print("Item not found in cart. Nothing modified.")

    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        total = 0

        for item in self.cart_items:
            total += item.item_quantity

        return total

    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        total = 0

        for item in self.cart_items:
            total += item.item_price * item.item_quantity

        return total

    # Outputs total of objects in cart.
    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Number of Items: " + str(self.get_num_items_in_cart()))
        print()
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print()
        print("Total: $" + str(self.get_cost_of_cart()))

    # Outputs each item's description.
    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)


# Prints the menu
def print_menu(shopping_cart):
    menu = ("\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n")

    command = ""

    # Loop until user quits using 'q' command
    while command != "q":
        print(menu)
        command = input("Choose an option: ")

        # Validate input command
        while command not in ["a", "r", "c", "i", "o", "q"]:
            command = input("Choose an option: ")

        # Add a new item to cart
        if command == "a":
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))

            item = ItemToPurchase()
            item.item_name = item_name
            item.item_description = item_description
            item.item_price = item_price
            item.item_quantity = item_quantity

            shopping_cart.add_item(item)

        # Remove an item from the cart
        elif command == "r":
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")

            shopping_cart.remove_item(item_name)

        # Change an item's quantity based on the item's name
        elif command == "c":
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            item_quantity = int(input("Enter the new quantity: "))

            item = ItemToPurchase()
            item.item_name = item_name
            item.item_quantity = item_quantity

            shopping_cart.modify_item(item)

        # Print item descriptions
        elif command == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()

        # Print shopping cart
        elif command == "o":
            print("\nOUTPUT SHOPPING CART")
            shopping_cart.print_total()


def main ():
    customer_name = input("Enter Customer's Name: ")
    current_date = input("Enter Today's Date: ")
    print()
    print("Customer Name: " + customer_name)
    print("Today's Date: " + current_date)
    print()

    shopping_cart = ShoppingCart(customer_name, current_date)

    print_menu(shopping_cart)

    return


if __name__ == "__main__":
    main()

