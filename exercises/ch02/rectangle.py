#!/usr/bin/env python3

# display a welcome message
print("The Rectangle program")
print()

# get input from the user
length= float(input("Enter length of rectangle:\t\t"))
width = float(input("Enter width of rectangle:\t"))

# calculate area of rectangle
area = length * width
area = round(area, 2)

# calculate perimeter of rectangle
perimeter = (2*length) + (2*width)
perimeter = round(perimeter, 2)
            
# format and display the result
print()
print("Area:", area,
        "\nPerimeter:", perimeter)
print()
print("Bye!")


