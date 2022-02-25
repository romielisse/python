#!/usr/bin/env python3

from datetime import datetime, timedelta

def main():
    print("Arrival Time Estimator")
    print()

    date_format = "%Y-%m-%d"
    time_format = "%I:%M %p"

    choice = "y"
    while choice.lower() == "y":
        # get departure date/time
        dep_date_str = input("Estimated date of departure (YYYY-MM-DD): ")    
        dep_time_str = input("Estimated time of departure (HH:MM AM/PM): ")

        # convert str to datetime
        dep_str = dep_date_str + " " + dep_time_str
        dep_datetime = datetime.strptime(dep_str,
                                         date_format + " " + time_format)

        # get miles / mph
        miles = int(input("Enter miles: "))
        miles_per_hour = int(input("Enter miles per hour: "))
        print()

        # perform the calculations 
        hours = miles // miles_per_hour
        remaining_miles = miles % miles_per_hour
        miles_per_minute = miles_per_hour / 60
        minutes = remaining_miles / miles_per_minute
        minutes = int(minutes)
        travel_time = timedelta(hours=hours, minutes=minutes)
        arr_datetime = dep_datetime + travel_time

        # display travel time and eta
        print("Estimated travel time")
        print("Hours:", hours)
        print("Minutes:", minutes)
        print(f"Estimated date of arrival: {arr_datetime:{date_format}}")
        print(f"Estimated time of arrival: {arr_datetime:{time_format}}")
        print()
        
        # ask if user wants to continue
        choice = input("Continue? (y/n): ")
        print()
        
    print("Bye!")    

if __name__ == "__main__":
    main()
