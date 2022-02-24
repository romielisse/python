#!/usr/bin/env python3

# display a welcome message
print("Tip Calculator")
print()

# get input from the user
meal_cost = float(input("Cost of meal: "))
tip_percent = float(input("Tip percent:  "))
print()

# calculate tip and total amount
tip_amount = round(meal_cost * (tip_percent / 100), 2)
total = round(meal_cost + tip_amount, 2)

# display the results
print("Tip amount:  ", tip_amount)
print("Total amount:", total)
