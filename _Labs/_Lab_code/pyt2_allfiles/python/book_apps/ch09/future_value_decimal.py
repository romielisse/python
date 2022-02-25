#!/usr/bin/env python3

from decimal import Decimal
import locale as lc

def get_future_value(monthly_investment, yearly_interest, years):
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12
    future_value = Decimal("0.00")
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    future_value = future_value.quantize(Decimal("1.00"))
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get user input and future value
        monthly_investment = Decimal(input("Enter monthly investment:   "))
        yearly_interest = Decimal(input("Enter yearly interest rate: "))
        years = int(input("Enter number of years:      "))
        future_value = get_future_value(
            monthly_investment, yearly_interest, years)
        print()

        # format and display the results
        lc.setlocale(lc.LC_ALL, "en_US")
        monthly_investment = lc.currency(monthly_investment, grouping=True)
        future_value = lc.currency(future_value, grouping=True)
        
        s1 = 20
        s2 = ">10"
        print(f"{'Monthly investment:':{s1}} {monthly_investment:{s2}}")
        print(f"{'Interest rate:':{s1}} {yearly_interest:{s2}}")
        print(f"{'Years:':{s1}} {years:{s2}}")
        print(f"{'Future value:':{s1}} {future_value:{s2}}")
        print()


        choice = input("Continue? (y/n): ")
        print()

if __name__ == "__main__":
    main()
