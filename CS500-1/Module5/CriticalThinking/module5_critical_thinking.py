## Prompts the user for input and returns the value.
# f the value is not a valid number, it will prompt the user again
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


# Part 1:
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
def part_1():
    print("*----------------------------------------*")
    print("Part 1: This program will calculate the average rainfall over a period of years")
    print()

    # get the number of years from the user
    years = int(get_user_input("Enter the number of years: "))

    # calculate the total months from the number of years
    total_months = years * 12

    # initialize the total rainfall to 0, we will add to this as we go
    total_rainfall = 0

    # outer loop - iterate once for each year
    for year in range(1, years + 1):
        # inner loop - iterate once for each month
        for month in range(1, 12 + 1):
            # get the rainfall for the month from the user
            total_rainfall += get_user_input(
                "Enter the rainfall for month " + str(month) + " of year " + str(year) + ": ", True)

    # calculate the average rainfall
    average_rainfall = total_rainfall / total_months

    print()
    print("Total Months: " + str(total_months))
    print("Total Rainfall: " + str(total_rainfall))
    print("Average Rainfall Per Month: " + str(average_rainfall))
    print("*----------------------------------------*")
    print()


# Part 2:
# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:
#
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
def part_2():
    print("*----------------------------------------*")
    print("Part 2: This program will calculate the number of points awarded for a book club")
    print()

    # get the number of books from the user
    books = int(get_user_input("Enter the number of books purchased this month: "))

    # initialize the points to 0
    points = 0

    # determine the number of points based on the number of books purchased
    if books < 2:
        points = 0
    elif books < 4:
        points = 5
    elif books < 6:
        points = 15
    elif books < 8:
        points = 30
    elif books >= 8:
        points = 60

    print()
    print("Points Awarded: " + str(points))
    print("*----------------------------------------*")
    print()


# Main function, runs the program
def main():
    part_1()
    part_2()
    print()


if __name__ == "__main__":
    main()
