#!/usr/bin/env python3

def display_title():
    print("Prime Number Checker")
    print()

def get_valid_int():
    while True:
        num = int(input("Please enter an integer between 1 and 5000: "))
        if num <= 1 or num >= 5000:
            print("Invalid integer. Please try again.")
        else:
            return num

def get_factors(num):
    factors = []
    # this loop includes 1 and num
    for i in range(1, num+1):
        remainder = num % i
        if remainder == 0:
            factors.append(i)
    return factors

def main():
    display_title()
    
    again = 'y'
    while again == 'y':
        num = get_valid_int()
        factors = get_factors(num)
        if len(factors) == 2:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is NOT a prime number.")
            print(f"It has {len(factors)} factors:", end=" ")
            for factor in factors:
                print(factor, end=" ")
            print()
        print()
        
        again = input("Try again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
