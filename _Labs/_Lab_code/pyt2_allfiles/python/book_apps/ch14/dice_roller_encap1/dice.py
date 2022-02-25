import random
from dataclasses import dataclass

@dataclass
class Die:
    __value:int = 1

    def getValue(self):
        return self.__value
                
    def setValue(self, value):
        if value < 1 or value > 6:
            raise ValueError("Die value must be from 1 to 6.")
        else:
            self.__value = value
                
    def roll(self):
        self.__value = random.randrange(1, 7)

                
class Dice:
    # use explicit initializer because @dataclass doesn't allow
    # attributes with a default value that's mutable (like list)
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)
                
    def rollAll(self):
        for die in self.__list:
            die.roll()

    # return a tuple of Die objects to prevent
    # the calling code from getting a reference to 
    # the list of Dice objects and modifying them
    def viewAll(self):
        return tuple(self.__list)
