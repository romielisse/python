#!/usr/bin/env python3

from dataclasses import dataclass
import random

ROSHAMBO_LIST = ["rock", "paper", "scissors"]

@dataclass
class Player:
    name:str = ""
    roshambo:str = ROSHAMBO_LIST[0] # default to 'rock'

    # default behavior - always generate Roshambo of 'rock'
    def generateRoshambo(self):
        self.__roshambo = ROSHAMBO_LIST[0] 

    def play(self, other_player):
        if self.roshambo == other_player.roshambo:
            return None
        else:
            if self.roshambo == "rock" and other_player.roshambo == "scissors" \
            or self.roshambo == "paper" and other_player.roshambo == "rock" \
            or self.roshambo == "scissors" and other_player.roshambo == "paper":
                return self
            else:
                return other_player

    def __str__(self):
        return f"{self.name}: {self.roshambo}"

@dataclass
class Bart(Player):
    def __post_init__(self):
        self.name = "Bart"

@dataclass
class Lisa(Player):
    def __post_init__(self):
        self.name = "Lisa"

    # override superclass default behavior to generate random Roshambo
    def generateRoshambo(self):
        self.roshambo = random.choice(ROSHAMBO_LIST) # random choice
        
def main():
    print("Roshambo Game\n")

    name = input("Enter your name: ")
    print()
    
    player1 = Player(name)

    opponent = input("Would you like to play Bart or Lisa? (b/l): ")
    print()

    if opponent.lower() == "b":
        player2 = Bart()
    elif opponent.lower() == "l":
        player2 = Lisa()        

    again = "y"
    while again.lower() == "y":
        # set Roshambo for player 1
        selection = input("Rock, paper, or scissors? (r/p/s): ").lower()
        print()
        
        if selection == "r":
            player1.roshambo = "rock"
        elif selection == "p":
            player1.roshambo = "paper"
        elif selection == "s":
            player1.roshambo = "scissors"
        else:
            print("Invalid choice. Try again.")
            continue

        # generate Roshambo for player 2
        player2.generateRoshambo()

        # display names and Roshambos
        print(player1)
        print(player2)

        # play game and display winner
        winner = player1.play(player2)
        if winner is None:
            print("Draw!\n")
        else:
            print(f"{winner.name} wins!\n")

        again = input("Play again? (y/n): ")
        print()

    print("Thanks for playing!")
 

if __name__ == "__main__":
    main()
