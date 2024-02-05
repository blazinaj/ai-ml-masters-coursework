def main():

    # valid course numbers
    valid_course_numbers = ["CSC101", "CSC102", "CSC103", "NET110", "COM241"]

    # create the dictionary for the room numbers
    room_numbers = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    # create the dictionary for the instructors
    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    # create the dictionary for the meeting times
    meeting_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    # get user input until there's a valid course number
    while True:
        # get the course number from the user
        course_number = input("Enter the course number: ")

        # check if the course number is valid
        if course_number in valid_course_numbers:
            break
        else:
            print("The course number is invalid, please try again.")

    # display the course's room number, instructor, and meeting time
    print("Room Number: " + room_numbers[course_number])
    print("Instructor: " + instructors[course_number])
    print("Meeting Time: " + meeting_times[course_number])


if __name__ == "__main__":
    main()

