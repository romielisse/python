#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
#mpg = miles_driven / gallons_used
#mpg = round(mpg, 2)
mpg = round((miles_driven / gallons_used), 1)
total_gas_cost = round(gallons_used * cost_per_gallon, 1)
cost_per_mile = round(total_gas_cost / miles_driven, 1)
                
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}"
      f"\nTotal Gas Cost:\t\t\t{total_gas_cost}"
      f"\nCost Per Mile:\t\t\t{cost_per_mile}")
print()
print("Bye!")


