# Ben Wynia
# Pig Latin Conversion
# COMPSCIX444.4__009
# 7/18/2021

# Write a program in Python 3 that converts a sentence typed in by the user to Pig Latin.
# Pig Latin has two rules:
#
# If a word begins with a consonant all consonants before the first vowel are moved to the end of the word and
# the letters "ay" are then added to the end. e.g. "coin" becomes "oincay" and "flute" becomes "uteflay".
# If a word begins with a vowel then "yay" is added to the end. e.g."egg" becomes "eggyay" and "oak" becomes "oakyay".

def message_encoder(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list_of_words = message.split()

    pig_latin = ''
    for word in list_of_words:
        # word begins with vowel
        if word[0] in vowels:
            pig_latin += word + 'yay' + ' '
        # word begins with a consonant
        else:
            # need to handle situation where multiple consonants in a row
            for letter in word:
                # iterates until it finds a vowel, then adds all previous letters in word to end and appends 'ay'
                if letter in vowels:
                    pig_latin += word[word.index(letter):len(word)] + word[0:word.index(letter)] + 'ay' + ' '
                    break
    return(pig_latin)

while True:
    # Get user input
    print('Please enter a message to be converted to pig latin code, or type "exit":')
    user_input= input()
    if user_input == "exit":
        break
    print(message_encoder(user_input))
