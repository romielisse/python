from dataclasses import dataclass

@dataclass
class Product:
    # three attributes with default values
    name:str = ""                                 # attribute 1
    price:float = 0.0                             # attribute 2
    discountPercent:float = 0                     # attribute 3

    '''
    # the initializer method that Python generates based on above
    def __init__(self, name="", price=0.0, discountPercent=0):
        self.name = name                          # attribute 1
        self.price = price                        # attribute 2
        self.discountPercent = discountPercent    # attribute 3
    '''

    # a method that uses two attributes to perform a calculation
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    # a method that calls another method to perform a calculation
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
