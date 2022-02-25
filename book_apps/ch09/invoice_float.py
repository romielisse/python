#!/usr/bin/env python3

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    # get the user entry
    order_total = float(input("Enter order total: "))
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = 0
    elif order_total >= 100 and order_total < 250:
        discount_percent = .1
    elif order_total >= 250:
        discount_percent = .2
            
    # calculate the results
    discount = order_total * discount_percent
    subtotal = order_total - discount
    sales_tax = subtotal * .05
    invoice_total = subtotal + sales_tax

##    # calculate the results (this works)
##    discount = round(order_total * discount_percent, 2)
##    subtotal = order_total - discount
##    sales_tax = round(subtotal * .05, 2)
##    invoice_total = subtotal - sales_tax
    
    # display the results
    print(f"Order total:        {order_total:10,.2f}")
    print(f"Discount amount:    {discount:10,.2f}")
    print(f"Subtotal:           {subtotal:10,.2f}")
    print(f"Sales tax:          {sales_tax:10,.2f}")
    print(f"Invoice total:      {invoice_total:10,.2f}")
    print()

    choice = input("Continue? (y/n): ")
    print()
    
print("Bye!")
