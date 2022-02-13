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
    if len(word)==0:
        return word
    else:
        return reverse(word[1:]) + word[0]

# User input
while True:
    # Get user input
    print('Enter a word, or enter "exit" to quit:')
    user_input = input()

    # test if user tried to quit program
    if user_input.lower() == "exit":
        break
    try:
        print("Original Word: %s" % user_input)
        reversed_word = reverse(user_input)
        print("Reversed Word: %s" % reversed_word)
    except:
        print("Unexpected exception. Please re-enter your word.")