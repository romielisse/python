def display_title():
    print("The Wizard Inventory program")
    print()    

def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def show(inventory):
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item}")
    print()

def grab_item(inventory):
    if len(inventory) >= 4:
        print("You can't carry any more items. Drop something first.\n")
    else:
        item = input("Name: ")
        inventory.append(item)
        print(f"{item} was added.\n")

def edit_item(inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("Invalid item number.\n")
    else:
        item = input("Updated name: ")
        inventory[number-1] = item
        print(f"Item number {number} was updated.\n")

def drop_item(inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("Invalid item number.\n")
    else:
        item = inventory.pop(number-1)
        print(f"{item} was dropped.\n")

def main():
    display_title()
    display_menu()

    # all players start with these 3 items
    inventory = ["wooden staff", "wizard hat",
                 "cloth shoes"]

    while True:        
        command = input("Command: ")        
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab_item(inventory)
        elif command == "edit":
            edit_item(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
