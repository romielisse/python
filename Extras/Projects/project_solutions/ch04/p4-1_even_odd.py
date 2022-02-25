#!/usr/bin/env python3

# the add function
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# the main function
def main():
    print("Even or Odd Checker")
    print()
    my_num = int(input("Enter an integer:  "))
    if is_even(my_num):
        print("This is an even number.")
    else:
        print("This is an odd number.")

if __name__ == "__main__":
    main()
