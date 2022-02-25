#!/usr/bin/env python3

# display a welcome message
print("Price Comparison")
print()

# display actual cost
price_64_oz = float(input("Price of 64 oz size: "))
price_32_oz = float(input("Price of 32 oz size: "))
print()

# calculate unit price
price_per_oz_64 = round(price_64_oz / 64, 2)
price_per_oz_32 = round(price_32_oz / 32, 2)

# display the results
print("Price per oz (64 oz):", price_per_oz_64)
print("Price per oz (32 oz):", price_per_oz_32)
