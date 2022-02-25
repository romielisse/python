#!/usr/bin/env python3

import random
from dataclasses import dataclass

@dataclass
class Card:
    rank:str
    suit:str
    value:int

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

class Deck:
    def __init__(self):
        self.__deck = []

        ranks = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                 "Jack", "Queen", "King")
        suits = ("Clubs", "Diamonds", "Hearts", "Spades")

        for suit in suits:
            for rank in ranks:
                if rank == "Ace":
                    value = 11
                elif rank == "Jack" or rank == "Queen" or rank == "King":
                    value = 10
                else:
                    value = int(rank)           
                self.__deck.append(Card(rank, suit, value))

    @property
    def count(self):
        return len(self.__deck)
        
    def shuffle(self):
        random.shuffle(self.__deck)

    def dealCard(self):
        return self.__deck.pop()

    def __iter__(self):
        for card in self.__deck:
            yield card
    
    
class Hand:
    def __init__(self):
        self.__cards = []

    def addCard(self, card):
        self.__cards.append(card)

    @property
    def count(self):
        return len(self.__cards)

    @property
    def points(self):
        points = 0
        for card in self.__cards:
            points += card.value
        if points > 21:
            ace_count = 0
            for card in self.__cards:
                if card.rank == "Ace":
                    ace_count += 1
            points = points - (ace_count * 10)
        return points

    @property
    def isBlackjack(self):
        return self.count == 2 and self.points == 21
        ''' same as
        if self.count == 2 and self.points == 21:
            return True
        else:
            return False
        '''
    @property
    def isBusted(self):
        return self.points > 21
        

    def __iter__(self):
        for card in self.__cards:
            yield card

            
def main():
    print("Cards - Tester")
    print()

    # test deck
    print("DECK")
    deck = Deck()
    for card in deck:
        print(card)

    deck.shuffle()
    print("Deck count:", deck.count)
    print()


    # test hand
    print("HAND")
    hand = Hand()
    for i in range(4):
        hand.addCard(deck.dealCard())

    for card in hand:
        print(card)

    print("Hand points:", hand.points)
    print("Hand count:", hand.count)
    print("Deck count:", deck.count)
    print()


if __name__ == "__main__":
    main()