# Ben Wynia
# Number Sorter
# COMPSCIX444.4__009
# 7/18/2021

# Write an application in Python 3 that prompts the user to enter a list of comma separated numbers,
# sorts those numbers using the insertion sort algorithm, and calculates the mean value of the list.
# The insertion sort that works in the same way that you would typically sort playing cards in your
# hand by finding the correct place of the each number in the list one at a time from left to right.
# Insertion sorts follow the following steps:
# Step 1: Set the second number in the list
# Step 2: Compare that number with each of the previous numbers in the list, swapping them if they are in the wrong order.
# Step 3: Once all the previous numbers are in the correct order advance to the next number in the list.
# Step 4: Repeat Steps 2 and 3 until the list is in the correct order.
from statistics import mean

def sorting_algorithm(list):
    swap_count = 0
    for item in range(1, len(list)):

        # value to analyze and move
        value = list[item]

        # index of previous item in list to compare to
        prev = item - 1
        while value < list[prev] and prev >= 0:
            # swap value and previous value
            list[prev + 1] = list[prev]
            prev -= 1
            list[prev + 1] = value

            # update the swap count, print results
            swap_count += 1
            string_list=[str(x) for x in list]
            print("Swap %s: %s" % (swap_count, ((', '.join(string_list)))))
    return(list)

while True:
    # Get user input
    print('Enter a list of comma separated numbers, or enter "exit" to quit:')
    user_input = input()

    # test if user tried to quit program
    if user_input.lower() == "exit":
        break

    # convert list elements to int
    try:
        # convert string to list
        parsed_input = list(user_input.split(","))
        for i in range(0,len(parsed_input)):
            parsed_input[i]=int(parsed_input[i])

        # run the sorting algorithm
        sorted_list = sorting_algorithm(parsed_input)
        string_list = [str(x) for x in sorted_list]

        # Print sorted list and mean value
        original_list = [str(x) for x in parsed_input]
        print("Original List: %s" % ((', '.join(original_list))))
        print("Sorted List: %s" % ((', '.join(string_list))))
        print("Mean Value: %s" % (mean(sorted_list)))

    except:
        print("Your entry was not valid, please try again.")
