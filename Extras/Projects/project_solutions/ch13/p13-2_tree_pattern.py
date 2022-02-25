def main():
    print("Tree Pattern")
    print()

    num = int(input("Enter the number of branches: "))
    print()
    
    branch(num)

def branch(num):
    multiplier = 5
    if num == 0:
        return
    else:
        branch(num-1)
        print(num, "*" * num * multiplier)
        branch(num-1)

if __name__ == "__main__":
    main()
