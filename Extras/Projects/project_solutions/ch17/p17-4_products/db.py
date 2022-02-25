import sys
import os
import sqlite3
from contextlib import closing

from objects import Category
from objects import Product

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "guitar_shop.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_category(row):
    return Category(row["categoryID"], row["categoryName"])

def make_product(row):
    return Product(row["productID"], row["productCode"], row["productName"], row["listPrice"],
            make_category(row))

def get_categories():
    query = '''SELECT categoryID, categoryName
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories

def get_products_by_category(category_name):
    query = '''SELECT productID, productCode, productName, listPrice,
                      Product.categoryID as categoryID, categoryName
               FROM Product JOIN Category
                      ON Product.categoryID = Category.categoryID
               WHERE categoryName = ?
               ORDER BY productName'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_name,))
        results = c.fetchall()

    products = []
    for row in results:
        products.append(make_product(row))
    return products

def get_product_by_code(product_code):
    query = '''SELECT productID, productCode, productName, listPrice,
                      Product.categoryID as categoryID, categoryName
               FROM Product JOIN Category
                      ON Product.categoryID = Category.categoryID
               WHERE productCode = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (product_code,))
        row = c.fetchone()
        if row:
            return make_product(row)
        else:
            return None

def update_product(product):
    sql = '''UPDATE Product
             SET listPrice = ?
             WHERE productCode = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (product.price, product.code))
        conn.commit()

def main():
    connect()
    
    print("CATEGORIES")
    categories = get_categories()
    for cat in categories:
        print(cat.name)

    print("PRODUCTS BY CATEGORY - BASSES")
    products = get_products_by_category("Basses")
    for product in products:
        print(product.name)

    print("PRODUCT BY CODE - tama")
    product = get_product_by_code("tama")
    print(product)

    print("PRODUCT BY CODE - bad_code")
    product = get_product_by_code("bad_code")
    print(product)

if __name__ == "__main__":
    main()
