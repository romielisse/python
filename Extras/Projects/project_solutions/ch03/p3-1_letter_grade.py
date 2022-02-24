#!/usr/bin/env python3

# display a welcome message
print("Letter Grade Converter")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    number = int(input("Enter numerical grade: "))

    # convert number to letter
    if number > 87:
        letter = "A"
    elif number > 79:
        letter = "B"
    elif number > 66:
        letter = "C"
    elif number > 59:
        letter = "D"
    else:
        letter = "F"

    # display letter
    print("Letter grade:", letter)
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)?: ")
    print()

print("Bye!")
