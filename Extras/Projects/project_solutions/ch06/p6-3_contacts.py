#!/usr/bin/env python3

def display(contacts):
    if len(contacts) == 0:
        print("There are no contacts in the list.\n")
        return
    else:
        for i, row in enumerate(contacts, start=1):
            print(f"{i}. {row[0]}")
        print()

def add(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    
    print(f"{contact[0]} was added.")   
    print()

def view(contacts):
    number = int(input("Number: "))
    if number < 1 or number > len(contacts):
        print("Invalid contact number.\n")
    else:
        contact = contacts[number-1]
        print("Name:", contact[0])
        print("Email:", contact[1])
        print("Phone:", contact[2])
        print()
      
def delete(contacts):
    number = int(input("Number: "))
    if number < 1 or number > len(contacts):
        print("Invalid contact number.\n")
    else:
        contact = contacts.pop(number-1)
        print(f"{contact[0]} was deleted.\n")
      
def display_title():
    print("Contact Manager")
    print()

def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add  - Add a contact")
    print("del  - Delete a contact")
    print("exit - Exit program")
    print()    

def main():
    contacts = [["Guido van Rossum", "guido@python.org", "+31 0474 33 88 26"],
                ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]

    display_title()
    display_menu()
    
    while True:
        command = input("Command: ")
        if command == "list":
            display(contacts)
        elif command == "view":
            view(contacts)
        elif command == "add":
            add(contacts)
        elif command == "del":
            delete(contacts)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
