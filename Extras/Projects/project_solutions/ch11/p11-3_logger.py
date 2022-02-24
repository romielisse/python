#!/usr/bin/env python3

from datetime import datetime

FILENAME = "future_value_log.txt"

def log(monthly_investment, yearly_interest, years, future_value):
    current_date = datetime.now()    
    with open(FILENAME, "a") as file:
        file.write(f"{current_date:%Y-%m-%d %H:%M:%S} - ")
        file.write(f"{monthly_investment}|{yearly_interest}|" + 
                   f"{years}|{future_value}\n")
        
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    future_value = round(future_value, 2)

    log(monthly_investment, yearly_interest, years, future_value)
    
    return future_value

def main():
    print("Future Value Calculator")
    print()
    
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t"))
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        years = int(input("Enter number of years:\t\t"))

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print(f"Future value:\t\t\t{future_value:,.2f}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
