#!/usr/bin/env python3
        
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

        monthly_investment = 0.0
        yearly_interest_rate = 0.0
        years = 0

        while(monthly_investment <= 0):
            monthly_investment = float(input("Enter monthly investment:\t"))
            if(monthly_investment <= 0):
                print("Entry must be greater than 0. Please try again.")

        while(yearly_interest_rate <= 0 or yearly_interest_rate > 15):
            yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
            if(yearly_interest_rate <= 0 or yearly_interest_rate > 15):
                print("Entry must be greater than 0 and less than or equal to 15. Please try again.")

        while(years <= 0 or years > 50):
            years = int(input("Enter number of years:\t\t"))
            if(years <= 0 or years > 50):
                print("Entry must be greater than 0 and less than or equal to 50. Please try again.")

        # get and display future value
        count = 0

        while(count < years):
            count += 1
            future_value = calculate_future_value(
                monthly_investment, yearly_interest_rate, count)

            print(f"Year = {count}\t\tFuture value = {round(future_value, 2)}")

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
