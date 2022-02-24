#!/usr/bin/env python3

def get_cost():
    while True:
        try:
            meal_cost = float(input("Cost of meal: "))
        except ValueError:
            print("Must be valid decimal number. Please try again.")
            continue

        if meal_cost <= 0:
            print("Must be greater than 0. Please try again.")
        else:
            return meal_cost

def get_tip_percent():
    while True:
        try:
            tip_percent = int(input("Tip percent:  "))
        except ValueError:
            print("Must be valid integer. Please try again.")
            continue

        if tip_percent <= 0:
            print("Must be greater than 0. Please try again.")
        else:
            return tip_percent

def main():
    # display a welcome message
    print("Tip Calculator")
    print()

    print("INPUT")
    meal_cost = get_cost()
    tip_percent = get_tip_percent()
    print()

    # calculate tip and total amount
    tip_amount = round(meal_cost * (tip_percent / 100), 2)
    total = round(meal_cost + tip_amount, 2)

    print("OUTPUT")
    print("Cost of meal:", meal_cost)
    print("Tip percent: ", str(tip_percent) + "%")
    print("Tip amount:  ", tip_amount)
    print("Total amount:", total)

if __name__ == "__main__":
    main()
