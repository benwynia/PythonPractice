# Ben Wynia
# Mars Leap Year Calculator
# COMPSCIX444.4--009
# 7/11/2021

# The purpose of this program is to determine if a user-inputted year is a leap year on mars

# Create a loop to run the program until it is exited
print("This is the Mars Leap Year Calculator")
while True:
    # Get the user input
    print('Enter the Mars year to look up (or type exit): ')
    user_input = input()

    # Exit if the user typed some variation of "Exit"
    if user_input.lower() == "exit":
        break

    # Convert the user input from a string to an int. Except non-numeric text entry.
    try:
        user_input = int(user_input)
        if (user_input % 2 == 1 or user_input % 10 == 0):
            print("The year %s is a martian leap year" % user_input)
        else:
            print("The year %s is a not a martian leap year" % user_input)
    except ValueError:
        print("I don't understand your input, please try again")
