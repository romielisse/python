#!/usr/bin/env python3

import pickle

FILENAME = "birds.bin"

def write_birds(birds):
    with open(FILENAME, "wb") as file:
        pickle.dump(birds, file)

def read_birds():
    birds = {}
    try:
        with open(FILENAME, "rb") as file:
            birds = pickle.load(file)
        return birds
    except FileNotFoundError:
        return birds

def main():
    print("Bird Counter program")
    print()

    print("Enter 'x' to exit")
    print()
    
    birds = read_birds()
    while True:
        name = input("Enter name of bird: ").title()
        if name.lower() == "x": 
            break

        if name in birds:
            birds[name] += 1
        else:
            birds[name] = 1

    # write dictionary to file
    write_birds(birds)
    
    # sort names alphabetically
    names = list(birds.keys())
    names.sort()

    w1 = 25
    w2 = 5
    
    print()
    print(f"{'Name':{w1}} {'Count':{w2}}")
    print(f"{'='*w1} {'='*w2}")
    for name in names:
        count = birds[name]
        print(f"{name:{w1}} {count:<{w2}d}")

if __name__ == "__main__":
    main()
