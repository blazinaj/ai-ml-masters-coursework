# Step 1: Build the ItemToPurchase class with the following specifications:
#
# Attributes
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()


class ItemToPurchase:

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def calculate_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ " + "$" + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))


# Main function, runs the program
def main():

    item_1 = ItemToPurchase()

    item_1.item_name = input("Enter the item name: ")
    item_1.item_price = float(input("Enter the item price: "))
    item_1.item_quantity = int(input("Enter the item quantity: "))

    item_2 = ItemToPurchase()

    item_2.item_name = input("Enter the item name: ")
    item_2.item_price = float(input("Enter the item price: "))
    item_2.item_quantity = int(input("Enter the item quantity: "))

    print("TOTAL COST")

    item_1.print_item_cost()
    item_2.print_item_cost()

    total = item_1.calculate_cost() + item_2.calculate_cost()

    print("Total: $" + str(total))


if __name__ == "__main__":
    main()

