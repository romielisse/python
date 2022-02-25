import random
from dataclasses import dataclass

@dataclass
class Die:
    value:int = 1
                
    def roll(self):
        self.value = random.randrange(1, 7)

               
class Dice:
    # use explicit initializer because @dataclass doesn't allow
    # attributes with a default value that's mutable (like list)
    def __init__(self):
        self.list = []

    def addDie(self, die):
        self.list.append(die)
                
    def rollAll(self):
        for die in self.list:
            die.roll()
        
