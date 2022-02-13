# Get user input
print('Enter the measurement in centimeters:')
centimeters = input()

# Calculate conversion
inches= float(centimeters)/2.54
inches_rounded = "{:.2f}".format(inches)

# print result:
print("%s centimeters is equal to %s inches" % (centimeters, inches_rounded))