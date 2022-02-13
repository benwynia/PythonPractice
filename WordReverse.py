# Ben Wynia
# Word Reverse
# COMPSCIX444.4__009
# 8/8/2021

# Write a Python 3 application that contains a recursive user-defined function called reverse.
# The reverse function should reverse the order of the letters of any word passed to it.
#Your program should :
#- prompt the user to input a word
#- output the word string to the screen
#- output the reversed word to the screen

# Word Reversing Function
def reverse(word):
    reversed_word=""
    for i in range(0, len(word)):
        reversed_word += word[len(word)-i-1]
    return(reversed_word)

# User input
while True:
    # Get user input
    print('Enter a word, or enter "exit" to quit:')
    user_input = input()

    # test if user tried to quit program
    if user_input.lower() == "exit":
        break

    print("Original Word: %s" % user_input)
    reversed_word = reverse(user_input)
    print("Reversed Word: %s" % reversed_word)