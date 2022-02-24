import random
from dataclasses import dataclass

@dataclass
class Die:
    value:int = 0
                
    def roll(self):
        self.value = random.randrange(1, 7)

                
class Dice:
    # use traditional initializer bc @dataclass doesn't allow
    # attributes with mutable default (such as list)
    def __init__(self):
        self.all = []

    def addDie(self, die):
        self.all.append(die)
                
    def rollAll(self):
        for die in self.all:
            die.roll()
