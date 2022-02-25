#!/usr/bin/env/python3

import db
from objects import Product

def display_title():
    print("Product Manager")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()
    
    display_str = ""
    for category in categories:
        display_str += category.name + " | "
    display_str = display_str[:-3]
    print(display_str)
    print()

def display_menu():
    print("COMMAND MENU")
    print("view   - View products by category")
    print("update - Update product price")
    print("exit   - Exit program")
    print()    

def display_products_by_category():
    category_name = input("Category name: ").strip().title()
    products = db.get_products_by_category(category_name)

    print(f"{'Code':10s} {'Name':40s} {'Price':>10s}")
    print("-" * 62)
    for product in products:
        print(f"{product.code:10s} {product.name:40s}",
              f"{product.price:>10,.2f}")
       
    print()    

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")
            
def update_product():
    code = input("Product code: ").lower()
    price = get_float("New product price: ")
    product = db.get_product_by_code(code)
    if product:
        product.price = price
        db.update_product(product)
        print("Product updated.\n")
    else:
        print(f"Code '{code}' not in database - no action taken.\n")
        
def main():
    db.connect()
    display_title()
    display_categories()
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "view":
            display_products_by_category()
        elif command == "update":
            update_product()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
