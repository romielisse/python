import random
from dataclasses import dataclass

@dataclass
class Die:
    __value:int = 1

    @property  # read-only!
    def value(self):
        return self.__value
                
    def roll(self):
        self.__value = random.randrange(1, 7)

    # make it easier to get the value
    def __str__(self):
        return str(self.__value)
                
class Dice:
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)
                
    def rollAll(self):
        for die in self.__list:
            die.roll()

    def __iter__(self):
        for die in self.__list:
            yield die
    
