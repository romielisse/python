#!/usr/bin/env python3

# display program title
print("Table of Powers")
print()

# get input from the user
while True:
    start = int(input("Start number: "))
    stop  = int(input("Stop number:  "))
    if start > stop:
        print("Start number must be less than stop number. Please try again.\n")
        continue
    else:
        print()
        break

print("Number\tSquared\tCubed")
print("======\t=======\t=====")
for number in range(start, stop+1):
    print(f"{number}\t{number**2}\t{number**3}")
