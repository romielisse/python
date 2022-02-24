#!/usr/bin/env python3

def display_names(players):
    names = list(players.keys())
    names.sort()
    print("ALL PLAYERS: ")
    for name in names:
        print(name)
    print()


def display_stats(players):
    name = input("Enter a player name: ").title()
    if name in players.keys():
        player = players[name]
        print("Wins:   ", player["wins"])
        print("Losses: ", player["losses"])
        print("Ties:   ", player["ties"])
    else:
        print(f"There is no player named {name}.")
    print()

def main():
    print("Game Stats program")
    print()

    players = {
        "Joel": {"wins": 32, "losses": 14, "ties": 17},
        "Elizabeth": {"wins": 41, "losses": 3, "ties": 22},
        "Mike": {"wins": 8, "losses": 19, "ties": 11}
    }

    display_names(players)

    choice = "y"
    while choice.lower() == "y":
        display_stats(players)

        # ask if user wants to continue
        choice = input("Continue? (y/n): ")
        print()
        
    print("Bye!")     

if __name__ == "__main__":
    main()
