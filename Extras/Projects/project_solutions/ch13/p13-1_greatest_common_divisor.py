def main():
    print("Greatest Common Divisor")
    print()

    again = "y"
    while again.lower() == "y":
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))

        if num1 < num2:
            print("Number 1 must be greater than number 2. Try again.")
            continue

        print("Greatest common divisor:", gcd(num1, num2))
        print()

        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")


# a recursive function
def gcd(x, y):
    remainder = x % y
    if remainder == 0:
        return y
    else:
        return gcd(y, remainder)


if __name__ == "__main__":
    main()
