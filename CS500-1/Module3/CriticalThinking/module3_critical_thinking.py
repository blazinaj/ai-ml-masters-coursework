# Part 1
# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax.
# Display each of these amounts and the total price.

# Part 2
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
# Write a Python program to solve the general version of the above problem.
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

# Gets user input and validates it is a valid number. Allows for zero to be entered if allow_zero is True
def get_user_input(prompt, allow_zero=True):
    active = True

    while active:
        try:
            user_input = float(input(prompt))

            if user_input == 0 and not allow_zero:
                print("Zero is not allowed for this input")
                raise ValueError("Zero is not allowed for this input")

            return user_input
        except ValueError:
            print("Please enter a valid number")


TIP_PERCENTAGE = 0.18
SALES_TAX_PERCENTAGE = 0.07

# Gets the total tip amount
def get_tip_amount(charge):
    return charge * TIP_PERCENTAGE

# Gets the total sales tax amount
def get_sales_tax_amount(charge):
    return charge * SALES_TAX_PERCENTAGE


# Gets the total amount of the meal
def get_total_amount(charge):
    return charge + get_tip_amount(charge) + get_sales_tax_amount(charge)


def part_1():
    print("*----------------------------------------*")
    print("Part 1: This program will calculate the total amount of a meal purchased at a restaurant")
    print()

    charge = get_user_input("Enter Charge for Food: ")

    tip = get_tip_amount(charge)
    sales_tax = get_sales_tax_amount(charge)
    total = get_total_amount(charge)

    print()
    print("The tip amount is: " + str(tip))
    print("The sales tax amount is: " + str(sales_tax))
    print("The total amount is: " + str(total))
    print("*----------------------------------------*")
    print()

# Gets the time on a 24-hour clock when an alarm goes off
def calculate_time(current_time, hours_to_wait):
    return (current_time + hours_to_wait) % 24


def part_2():
    print("*----------------------------------------*")
    print("Part 2: This program will calculate the time on a 24-hour clock when an alarm goes off")
    print()

    current_time = get_user_input("Enter Current Time (in hours): ")
    hours_to_wait = get_user_input("Enter Hours to Wait for Alarm: ")

    alarm_time = calculate_time(current_time, hours_to_wait)

    print()
    print("The alarm will go off at: " + str(alarm_time))
    print("*----------------------------------------*")
    print()


# Main function, runs the program
def main():
    part_1()
    part_2()
    print()


if __name__ == "__main__":
    main()

    