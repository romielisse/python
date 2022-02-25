from dice import Die
from dataclasses import dataclass

@dataclass
class Game:
    __turn:int = 1
    __score:int = 0
    __scoreThisTurn:int = 0
    __isTurnOver:bool = False
    __isGameOver:bool = False
    __die:Die = Die()

    def play(self):
        while not self.__isGameOver:
            self.takeTurn()

    def takeTurn(self):
        print("TURN", self.__turn)
        self.__scoreThisTurn = 0
        self.__isTurnOver = False
        while not self.__isTurnOver:
            choice = input("Roll or hold? (r/h): ")
            if choice == "r":
                self.rollDie()
            elif choice == "h":
                self.holdTurn()
            else:
                print("Invalid choice. Try again.")

    def rollDie(self):
        self.__die.roll()
        print("Die:", self.__die.value)
        if self.__die.value == 1:
            self.__scoreThisTurn = 0
            self.__turn += 1
            self.__isTurnOver = True
            print("Turn over. No score.\n")
        else:
            self.__scoreThisTurn += self.__die.value

    def holdTurn(self):
        self.__score += self.__scoreThisTurn
        self.__isTurnOver = True
        print("Score for turn:", self.__scoreThisTurn)
        print("Total score:", self.__score, "\n")
        if self.__score >= 20:
            self.__isGameOver = True
            print("You finished in", self.__turn, "turns!")
        else:
            self.__turn += 1
