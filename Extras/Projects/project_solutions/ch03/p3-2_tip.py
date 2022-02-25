#!/usr/bin/env python3

# display a welcome message
print("Tip Calculator")
print()

# get input from the user
meal_cost = float(input("Cost of meal: "))
print()

for tip_percent in range(15, 30, 5):
    print(f"{tip_percent}%")

    # calculate tip and total amount
    tip_percent = tip_percent / 100
    tip_amount = round(meal_cost * tip_percent, 2)
    total = round(meal_cost + tip_amount, 2)

    # display the results
    print("Tip amount:  ", tip_amount)
    print("Total amount:", total)
    print()
