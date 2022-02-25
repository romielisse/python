from dataclasses import dataclass

@dataclass
class Player:
    name:str
    wins:int = 0
    losses:int = 0
    ties:int = 0
    id:int = 0

    def getGames(self):
        games = self.wins + self.losses + self.ties
        return games

def main():
    player = Player("Joel")
    print(player.name, player.id, player.wins, player.getGames())    

if __name__ == "__main__":
    main()
