import random
from dataclasses import dataclass

@dataclass
class Die:
    __value:int = 1

    def __post_init__(self):
        self.__value = self.roll()

    @property
    def value(self):
        return self.__value
                
    @value.setter
    def value(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
        else:
            self.__value = value
                
    @property
    def image(self):
        if self.__value == 6:
            return " _____ \n" + \
                    "|o   o|\n" + \
                    "|o   o|\n" + \
                    "|o___o|"
        elif self.__value == 5:
            return " _____ \n" + \
                   "|o   o|\n" + \
                   "|  o  |\n" + \
                   "|o___o|"
        elif self.__value == 4:
            return " _____ \n" + \
                   "|o   o|\n" + \
                   "|     |\n" + \
                   "|o___o|"
        elif self.__value == 3:
            return " _____ \n" + \
                   "|o    |\n" + \
                   "|  o  |\n" + \
                   "|____o|"
        elif self.__value == 2:
            return " _____ \n" + \
                   "|o    |\n" + \
                   "|     |\n" + \
                   "|____o|"
        elif self.__value == 1:
            return " _____ \n" + \
                   "|     |\n" + \
                   "|  o  |\n" + \
                   "|_____|"
                
    def roll(self):
        self.__value = random.randrange(1, 7)
        return self.__value

         
class Dice:
    # use explicit initializer because @dataclass doesn't allow
    # attributes with a default value that's mutable (like list)
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)

    @property
    def list(self):
        return tuple(self.__list)
                
    def rollAll(self):
        for die in self.__list:
            die.roll()

    def getTotal(self):
        total = 0
        for die in self.__list:
            total += die.value
        return total
