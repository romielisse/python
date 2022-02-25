#!/usr/bin/env python3
    
def get_float(prompt, low, high):
    user_input = 0.0
    while(user_input <= low or user_input > high):
        user_input = float(input(prompt + ":\t"))
        if(user_input <= low or user_input > high):
            print(f"Entry must be greater than {low} and less than or equal to {high}. Please try again.")

    return user_input

def get_int(prompt, low, high):
    user_input = 0.0
    while(user_input <= low or user_input > high):
        user_input = int(input(prompt + ":\t"))
        if(user_input <= low or user_input > high):
            print(f"Entry must be greater than {low} and less than or equal to {high}. Please try again.")

    return user_input

def main():
    choice = "y"
    while choice.lower() == "y":

        float_num = get_float("Enter a decimal", 50, 100)
        int_num = get_int("Enter integer", 1, 5)

        # see if the user wants to continue
        choice = input("\nContinue? (y/n): ")
        print()
    
if __name__ == "__main__":
    main()
