"""

Python Project #3
CS 1030

@Author: Brady Miner
@Version: Temperature Conversion Table

This program will display a temperature conversion table for degrees Celsius to Fahrenheit from 0-100 degrees
in multiples of 10.


"""
# Title and structure for for table output

print("\nCelsius to Fahrenheit")
print("Conversion Table\n")
print("Celsius\t  Fahrenheit")


for celsius in range(0, 101, 10):  # loop degrees celsius from 0 to 100 in multiples of 10
    fahrenheit = (celsius * 9 / 5) + 32  # Formula to convert celsius to fahrenheit

    print("{}\t\t  {}".format(celsius, round(fahrenheit)))  # Format the data to display in the table
