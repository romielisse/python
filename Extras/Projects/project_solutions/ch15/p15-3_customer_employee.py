#!/usr/bin/env python3
from dataclasses import dataclass

@dataclass
class Person:
    firstName:str
    lastName:str
    email:str

    @property
    def fullName(self):
        return f"{self.firstName.title()} {self.lastName.title()}"

@dataclass
class Customer(Person):
    number:str

@dataclass
class Employee(Person):
    ssn:str
    
def main():
    print("Customer/Employee Data Entry")
    print()

    again = "y"
    while again.lower() == "y":
        choice = input("Customer or employee? (c/e): ")
        print()
        
        if choice == "c" or choice == "e":
            person = get_input(choice)
            print()
            display(person)
        else:
            print("Invalid choice. Try again.")
            continue
          
        again = input("Continue? (y/n): ")
        print()

    print("Bye!")

def get_input(choice):
    print("DATA ENTRY")
    
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    
    if choice == "c":
        number = input("Number: ")
        customer = Customer(first_name, last_name, email, number)
        return customer
    elif choice == "e":
        ssn = input("SSN: ")
        employee = Employee(first_name, last_name, email, ssn)
        return employee        

def display(person):
    if isinstance(person, Customer):
        print("CUSTOMER")
    elif isinstance(person, Employee):
        print("EMPLOYEE")
    else:
        print("PERSON")
        
    print("Name:       ", person.fullName)
    print("Email:      ", person.email)
    if isinstance(person, Customer):
        print("Number:     ", person.number)
    elif isinstance(person, Employee):
        print("SSN:        ", person.ssn)
    print()


if __name__ == "__main__":
    main()
