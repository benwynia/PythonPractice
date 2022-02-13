# Get user input
print('Enter the temperature in Celsius:')
celsius_temp = input()

# calculate result
fahrenheit= (9/5)*float(celsius_temp )+32
fahrenheit_temp = "{:.2f}".format(fahrenheit)

# print calculation result
print("%s celsius is equal to %s fahrenheit" % (celsius_temp, fahrenheit_temp))