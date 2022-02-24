#!/usr/bin/env python3

# display a welcome message
from unicodedata import decimal


print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter the cost of gas per gallion:\t"))

# calculate and round miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)
# mpg = round(mpg, 1) # exercise 2-1-4
# mpg = round(miles_driven / gallons_used, 1) # exercise 2-1-5

# calculate the total cost and cost per mile
total_cost = cost_per_gallon * gallons_used
total_cost = round(total_cost, 2)

cost_per_mile = total_cost / miles_driven
cost_per_mile = round(cost_per_mile, 2)

# display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Cost Per Mile:\t\t\t{cost_per_mile}")
print(f"Total Cost of Gas:\t\t{total_cost}")
print()
print("Bye!")


