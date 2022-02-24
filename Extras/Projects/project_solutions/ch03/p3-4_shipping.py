#!/usr/bin/env python3

# display a welcome message
print("===============================================================")
print("Shipping Calculator")
print("===============================================================")

choice = "y"
while choice.lower() == "y":

    # get input from the user
    cost_of_items = float(input("Cost of items ordered:  "))

    # make sure input is a positive number
    if cost_of_items < 0:
        print("You must enter a positive number. Please try again.")
        continue
    
    # get shipping cost
    if cost_of_items >= 75:
        shipping_cost = 0
    elif cost_of_items >= 50:
        shipping_cost = 9.95
    elif cost_of_items >= 30:
        shipping_cost = 7.95
    else:
        shipping_cost = 5.95
    
    # calculate total cost
    total_cost = round(cost_of_items + shipping_cost, 2)

    # display coins
    print("Shipping cost:         ", shipping_cost)
    print("Total cost:            ", total_cost)
    print()

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print("===============================================================")
        
print("Bye!")
