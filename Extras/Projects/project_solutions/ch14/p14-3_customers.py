#!/usr/bin/env python3

from dataclasses import dataclass

@dataclass
class Customer:
    id:str
    firstName:str
    lastName:str
    company:str
    address:str
    city:str
    state:str
    zip:str

    @property
    def fullName(self):
        return f"{self.firstName.title()} {self.lastName.title()}"

    @property
    def fullAddress(self):
        a = ""
        if self.company != "":
            a += f"{self.company}\n"
        a += f"{self.address}\n"
        a += f"{self.city}, {self.state} {self.zip}"
        return a
    
import csv

FILENAME = "customers.csv"

def get_customers():
    with open(FILENAME, "r", newline='') as file:
        reader = csv.reader(file)

        # create a list to store all Customer objects
        customers = []

        # read each row of the data
        for row in reader:
            if row[0].lower() == "cust_id": # skip first line
                continue

            # create a list of Customer objects
            customer = Customer(row[0].strip(),
                                row[1].strip(),
                                row[2].strip(),
                                row[3].strip(),
                                row[4].strip(),
                                row[5].strip(),
                                row[6].strip(),
                                row[7].strip())
            customers.append(customer)
        return customers

def find_customer_by_id(customers, cust_id):
    for customer in customers:
        if customer.id == cust_id:
            return customer
    return None

def main():
    print("Customer Viewer")
    print()

    customers = get_customers()

    again = "y"
    while again.lower() == "y":
        cust_id = input("Enter customer ID: ").strip()
        print()

        customer = find_customer_by_id(customers, cust_id)
        if customer == None:
            print("No customer with that ID.")
            print()
        else:
            print(customer.fullName)
            print(customer.fullAddress)
            print()
        
        again = input("Continue? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
