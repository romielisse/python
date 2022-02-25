#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")

# get input from the user
user_continue = "y"

while user_continue.lower() == "y":
    print()
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter the cost of gas per gallion: "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        
        # calculate the total cost and cost per mile
        total_cost = round(cost_per_gallon * gallons_used, 2)

        cost_per_mile = round(total_cost / miles_driven, 2)

        print()
        print(f"Miles Per Gallon:\t\t{mpg}")
        print(f"Cost Per Mile:\t\t\t{cost_per_mile}")
        print(f"Total Cost of Gas:\t\t{total_cost}")

    user_continue = input("\nGet entries for another trip (y/n)? ")

print()
print("Bye!")



