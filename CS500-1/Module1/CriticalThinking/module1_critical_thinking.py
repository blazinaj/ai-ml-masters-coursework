# Jacob Blazina - CSU Global - CS500-1 - Module 1 Critical Thinking - 12/13/2023
#
# Part 1:
# Write a Python program to find the addition and subtraction of two numbers.
# Ask the user to input two numbers (num1 and num2).
# Given those two numbers, add them together to find the output.
# Also, subtract the two numbers to find the output.
#
# Part 2:
# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2).
# Given those two numbers, multiply them together to find the output.
# Also, divide num1/num2 to find the output.


# Adds two numbers together
def add(num1, num2):
    if type(num1) != float or type(num2) != float:
        raise TypeError("num1 and num2 must be valid numbers")

    return num1 + num2


# Subtracts the second number from the first number
def subtract(num1, num2):
    if type(num1) != float or type(num2) != float:
        raise TypeError("num1 and num2 must be valid numbers")

    return num1 - num2


# Multiplies two numbers together
def multiply(num1, num2):
    if type(num1) != float or type(num2) != float:
        raise TypeError("num1 and num2 must be valid numbers")

    return num1 * num2


# Divides the first number by the second number. Does not allow division by zero.
def divide(num1, num2):
    if type(num1) != float or type(num2) != float:
        raise TypeError("num1 and num2 must be valid numbers")

    if num2 == 0:
        raise ZeroDivisionError("Due to the laws of physics, num2 cannot be zero")

    return num1 / num2


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


# Part 1 of the assignment, adds and subtracts two numbers
def part_1():
    print("*----------------------------------------*")
    print("Part 1: This program will add and subtract two user-inputted numbers")
    print()

    num1 = get_user_input("Enter First Number: ")
    num2 = get_user_input("Enter Second Number: ")

    sum_result = add(num1, num2)
    difference_result = subtract(num1, num2)

    print()
    print("The sum of the two numbers is: " + str(sum_result))
    print("The difference of the two numbers is: " + str(difference_result))
    print("*----------------------------------------*")
    print()


# Part 2 of the assignment, multiplies and divides two numbers
def part_2():
    print("*----------------------------------------*")
    print("Part 2: This program will multiply and divide two user-inputted numbers")
    print()

    num1 = get_user_input("Enter First Number: ")
    num2 = get_user_input("Enter Second Number: ", allow_zero=False)

    product_result = multiply(num1, num2)

    try:
        div_result = divide(num1, num2)
    except ValueError:
        print("You have entered an invalid number for division, this program will now exit. Please try again!")

    print()
    print("The product of the two numbers is: " + str(product_result))
    print("The quotient of the two numbers is: " + str(div_result))
    print("*----------------------------------------*")
    print()


# Main function, runs the program
def main():
    part_1()
    part_2()
    print()


if __name__ == "__main__":
    main()

