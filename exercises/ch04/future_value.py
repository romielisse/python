#!/usr/bin/env python3

import validation
        
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0

    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user

        monthly_investment = validation.get_float("Enter monthly investment", 0, 1000)
        yearly_interest_rate = validation.get_float("Enter yearly interest rate", 0, 15)
        years = validation.get_int("Enter number of years", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print(f"\nFuture value = {round(future_value, 2)}")

        # see if the user wants to continue
        choice = input("\nContinue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
