TAX_RATE = 0.06

def get_tax(total):
    tax = total * TAX_RATE
    return round(tax, 2)

def get_total_after_tax(total):
    total_after_tax = total + get_tax(total)
    return round(total_after_tax, 2)
