#!/usr/bin/env python3

def display_title():
    print("Hike Calculator")
    print()

def to_feet(miles):
    feet = miles * 5280
    feet = int(round(feet))
    return feet

def main():
    display_title()
    miles = float(input("How many miles did you walk?: "))
    feet = to_feet(miles)
    print(f"You walked {feet} feet.")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
