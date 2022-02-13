# Ben Wynia
# Morse Code Printer
# COMPSCIX444.4__009
# 7/11/2021

# The purpose of this program is to convert a string to morse code and print it to an LED

# Install required packages
import RPi.GPIO as GPIO
import time

print('This is the Morse Code Machine')

# Define a dictionary with key value pairs
morse_code_dictionary= { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
                         'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.'}

def encrypt_message(string, dictionary):
    morse_message=''
    for character in string:

        if character ==' ':
            morse_message += '  '
        else:
            morse_message += character + dictionary[character] + ' '
    return(morse_message)

# This function writes the output to the LED
# the function will turn the LED on for 0.5 seconds for a dot, and 1 second for a dash
# the function will rest 0.5 second between characters, 1 seconds between words
def write_output_to_led(message):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    for character in message:
        time.sleep(0.5)
        print(character)
        if character==' ':
            GPIO.output(11, False)
            time.sleep(1)
        if character=='.':
            # dot short sequence on LED
            GPIO.output(11, True)
            time.sleep(0.5)
            GPIO.output(11, False)
        if character=='-':
            # dash long sequence on LED
            GPIO.output(11, True)
            time.sleep(1)
            GPIO.output(11, False)
        else:
            GPIO.output(11, False)

while True:
    # Get user input
    print('Please enter a message to be converted to morse code, or type "exit":')
    user_string=input().upper()
    if user_string=="EXIT":
        break
    message = encrypt_message(user_string,morse_code_dictionary)
    write_output_to_led(message)
