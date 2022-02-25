#!/usr/bin/env python3

import random

class RandomIntList(list):
    def __init__(self, count=10, min=1, max=100):
        for i in range(count):
            number = random.randint(min, max)
            self.append(number)
            
    @property
    def count(self):
        return len(self)

    @property
    def total(self):
        total = 0
        for i in self:
            total += i
        return total

    @property
    def average(self):
        average = self.total / self.count
        return average

    def __str__(self):
        s = ""
        for i in self:
            s += str(i) + ", "
        s = s[:-2]
        return s
    
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again.")
            
def main():
    print("Random Integer List")
    print()

    count = get_int("How many random integers should the list contain?: ")
    print()

    again = "y"
    while again.lower() == "y":
        int_list = RandomIntList(count)
        
        print("Random Integers")
        print("===============")
        print("Integers: ", int_list)
        print("Count:    ", int_list.count)
        print("Total:    ", int_list.total)
        print("Average:  ", round(int_list.average, 3))
        print()

        again = input("Continue? (y/n): ").lower()
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
