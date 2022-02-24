#!/usr/bin/env python3

def display_welcome():
    print("The Quarterly Sales program")
    print()

def get_quarterly_sales():
    sales_list = []
    for i in range(4):
        sales = float(input(f"Enter sales for Q {i+1}: "))
        sales_list.append(sales)
    return sales_list

def process_sales(sales_list):
    # calculate total
    total = 0
    for sales in sales_list:
         total += sales
    total = round(total, 2)

    # get count
    count = len(sales_list)
    
    # calculate average
    average = total / count
    average = round(average, 2)

    # get min and max
    lowest_quarter = min(sales_list)    
    highest_quarter = max(sales_list)
                
    # format and display the result
    print()
    print("Total:             ", total)
    print("Average Quarter:   ", average)
    print("Lowest Quarter:    ", lowest_quarter)
    print("Highest Quarter:   ", highest_quarter)

def main():
    display_welcome()
    sales_list = get_quarterly_sales()
    process_sales(sales_list)

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
