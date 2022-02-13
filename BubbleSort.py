# Ben Wynia
# Bubble Sort in Python 3
# COMPSCIX444.4__009
# 8/8/2021

def BubbleSorter(list):
    original_list=list.copy()
    counter = 0
    for i in range(len(list) - 1):
        for j in range(0, len(list) - 1 - i):
            was_changed = 0
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                was_changed=1
        if was_changed == 1:
            counter +=1
            string_list = [str(x) for x in list]
            print("Swap %s: %s" % (counter, ((', '.join(string_list)))))
    return(original_list,list,counter)

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
        sorted_list = BubbleSorter(parsed_input)

        # Print the original list, sorted list, and counter
        original_list = [str(x) for x in sorted_list[0]]
        print("Original List: %s" % ((', '.join(original_list))))
        string_list = [str(x) for x in sorted_list[1]]
        print("Sorted List: %s" % ((', '.join(string_list))))
        print("Number of passes: %s" % (sorted_list[2]))
    except:
        print("Invalid input detected.")