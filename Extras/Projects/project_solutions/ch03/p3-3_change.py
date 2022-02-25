#!/usr/bin/env python3

# display a welcome message
print("Change Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    cents = int(input("Enter number of cents (0-99): "))
    print()

    # calculate the number of quarters
    quarters = cents // 25
    cents = cents % 25      # assign the remainder to the cents variable

    # calculate the number of dimes
    dimes = cents // 10
    cents = cents % 10      # assign the remainder to the cents variable

    # calculate the number of nickels and pennies
    nickels = cents // 5    # get number of nickels
    pennies = cents % 5     # get number of pennies    

    # display coins
    print("Quarters: ", quarters)
    print("Dimes:    ", dimes)
    print("Nickels:  ", nickels)
    print("Pennies:  ", pennies)
    print()

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
