from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    @property
    def discountAmount(self):
        amt = self.price * self.discountPercent / 100
        return round(amt, 2)

    @property 
    def discountPrice(self):
        p = self.price - self.discountAmount
        return round(p, 2)

@dataclass
class LineItem:
    product:Product = None
    quantity:int = 1

    @property
    def total(self):
        return self.product.discountPrice * self.quantity

class Cart:
    def __init__(self):
        self.__lineItems = []

    def addItem(self, item):
        self.__lineItems.append(item)

    def removeItem(self, index):
        self.__lineItems.pop(index)

    @property
    def total(self):
        total = 0.0
        for item in self.__lineItems:
            total += item.total
        return total

    @property
    def count(self):
        return len(self.__lineItems)

    def __iter__(self):
        for item in self.__lineItems:
            yield item
