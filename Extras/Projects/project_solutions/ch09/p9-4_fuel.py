#!/usr/bin/env python3

# This program computes the amount of fuel needed by a 1980 Cessna 172N
# to fly from one airport to another.

import math

def main():
    print("Aircraft Fuel Calculator\n")

    choice = "y"
    while choice.lower() == "y":
        # Get input from the user
        distance = int(input("Distance in nautical miles: "))

        # Calculate flight time
        knots_per_hour = 120
        flight_time = distance / knots_per_hour
        hours = distance // knots_per_hour
        distance = distance % knots_per_hour
        knots_per_minute = knots_per_hour / 60
        minutes = int(distance // knots_per_minute)

        # Calculate required fuel
        gallons_per_hour = 8.4
        reserve_time = .5
        fuel = gallons_per_hour * (flight_time + reserve_time)
        fuel = math.ceil(fuel * 10) / 10

        # Print the results
        print(f"Flight time: {hours} hour(s) and {minutes} minute(s)")    
        print(f"Required fuel: {fuel} gallons")
        print()

        # Continue?
        choice = input("Continue? (y/n): ")
        print()
        
    print("Bye!")       


if __name__ == "__main__":
    main()
