#!/usr/bin/env python3

# display a welcome message
print("Travel Time Calculator")
print()

# get input from the user
miles = int(input("Enter miles: "))
miles_per_hour = int(input("Enter miles per hour: "))
print()

# perform the calculations
hours = miles // miles_per_hour
minutes = miles % miles_per_hour

# display the results
print("Estimated travel time")
print("Hours:", hours)
print("Minutes:", minutes)
