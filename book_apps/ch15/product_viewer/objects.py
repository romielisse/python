from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

@dataclass
class Book(Product):
    author:str = ""

    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.author}"

@dataclass        
class Movie(Product):
    year:int = 0

    def getDescription(self):
        return f"{Product.getDescription(self)} ({self.year})"
