#!/usr/bin/env python3

# display a welcome message
print("Registration Form")
print()

# get input from the user
first_name = input("First name:\t")
last_name = input("Last name:\t")
birth_year = input("Birth year:\t")
print()

# create strings
name = f"{first_name} {last_name}"
temp_password = f"{first_name}*{birth_year}"

# display the results
print(f"Welcome {name}!")
print("Your registration is complete.")
print(f"Your temporary password is: {temp_password}")
    
