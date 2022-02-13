# Ben Wynia
# Celsius to Fahrenheit Calculator
# COMPSCIX444.4--009
# 7/11/2021

# The purpose of this program is to convert between Celsius and Fahrenheit
import re

# Create a loop to run the program until it is exited
print("This is the Celsius <> Fahrenheit Calculator")

while True:
    # Get the user input
    print('Please enter a value in either Fahrenheit or Celsius or type exit (Example: 28.1 Fahrenheit): ')
    user_input = input()

    # Exit if the user typed some variation of "Exit"
    if user_input.lower() == "exit":
        break
    try:
        # Parse input string into a temperature value and a unit field
        match = re.search('(?P<temp>[^\s]+) (?P<unit>\w+)', user_input)
        temp = float(match.group('temp'))
        unit = match.group('unit').lower()

        # Ensure that input contains a valid unit
        if unit not in ('fahrenheit','celsius'):
            raise Exception("Bad Unit")

        # If Fahrenheit, convert to celsius
        elif unit=='fahrenheit':
            temp_converted="{:.2f}".format((5/9)*(temp-32))
            print("%s in fahrenheit is equal to %s in celsius." % (temp, temp_converted))

        # If celsius, convert to fahrenheit
        else:
            temp_converted = "{:.2f}".format((9 / 5) * temp + 32)
            print("%s in celsius is equal to %s in fahrenheit." % (temp, temp_converted))

    # Catch improper user inputs
    except (Exception, ValueError, AttributeError) as e:
        print("I don't understand. Try again.")
