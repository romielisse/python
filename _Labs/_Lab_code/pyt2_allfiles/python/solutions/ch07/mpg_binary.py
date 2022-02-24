#!/usr/bin/env python3

import pickle

# a file in the current directory
FILENAME = "trips.bin"

def write_trips(trips):
    with open(FILENAME, "wb") as file:
        pickle.dump(trips, file)
        
def read_trips():
    trips = []
    with open(FILENAME, "rb") as file:
        trips = pickle.load(file)
    return trips

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def list_trips(trips):
    print("Distance\tGallons\t\tMPG")
    for i in range(0, len(trips)):
        trip = trips[i]
        print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")
    print()

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = read_trips()
    list_trips(trips)
    
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
            
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trip = [miles_driven, gallons_used, mpg]
        trips.append(trip)
        write_trips(trips)

        list_trips(trips)
        
        more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()

