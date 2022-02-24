#!/usr/bin/env python3

import csv

FILENAME = "world_cup_champions.txt"

def read_champions():
    champions = {}
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            year = row[0]
            country = row[1]
            if country in champions:
                data = champions[country]
                data[0] += 1         # update count
                data[1].append(year) # update years
            else:
                if country.lower() == "country":  # don't add header row to dictionary
                    pass
                else:
                    count = 1
                    years = []
                    years.append(year)
                    data = [count, years]
                    champions[country] = data
    return champions

def main():
    champions = read_champions()

    print("FIFA World Cup Winners")
    print()

    w1 = 15
    w2 = 5
    print(f"{'Country':{w1}} {'Wins':{w2}} {'Years':{w1}}")
    print(f"{'='*7:{w1}} {'='*4:{w2}} {'='*5:{w1}}")

    # sort names alphabetically
    countries = list(champions.keys())
    countries.sort()
    
    for country in countries:
        data = champions[country]
        count = data[0]
        years = data[1]
        years_str = ""
        for year in years:
            years_str += year + ", "
        years_str = years_str[:-2]
            
        print(f"{country:{w1}} {count:<{w2}d} {years_str:{w1}}")

if __name__ == "__main__":
    main()
