from temperature import Temp

def display_menu():
    print("The Convert Temperatures program")
    print()
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenhit")
    print()

def convert_temp():
    option = int(input("Enter a menu option: "))
    temp = Temp()
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        temp.setFahrenheit(f)
        print("Degrees Celsius:", temp.getCelsius())    
    elif option == 2:
        c = int(input("Enter degrees Celsius: "))
        temp.setCelsius(c)
        print("Degrees Fahrenheit:", temp.getFahrenheit())
    else:
        print("You must enter a valid menu number.")

def main():
    display_menu()
    
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        
        again = input("Convert another temperature? (y/n): ")
        print()
        
    print("Bye!")

if __name__ == "__main__":
    main()
