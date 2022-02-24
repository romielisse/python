#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter App")
print()

# get input from the user
length= float(input("Please enter the length:\t"))
width = float(input("Please enter the width:\t\t"))

# calculate area and perimeter
area = length * width
perimeter = (2 * length) + (2 * width)
area = round(area, 2)
perimeter = round(perimeter, 2)
            
# format and display the result
print()
print(f"Area = {area}")
print(f"Perimeter = {perimeter}")
print()
print("Bye!")


