#!/usr/bin/env/python3

import db
from objects import Player

def display_title():
    print("Player Manager")
    print()    

def display_menu():
    print("COMMAND MENU")
    print("view - View players")
    print("add  - Add a player")
    print("del  - Delete a player")
    print("exit - Exit program")
    print()    

def display_players():
    players = db.get_players()
    print(f"{'Name':10}{'Wins':>10}{'Losses':>10}{'Ties':>10}{'Games':>10}")
    print("-" * 50)
    for player in players:
        print(f"{player.name:10}{player.wins:10d}{player.losses:10d}" + \
              f"{player.ties:10d}{player.getGames():10d}")
    print()

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again.")
            continue

        if value < 0:
            print("Number may not be less than zero. Please try again.")
        else:
            return value

def add_player():
    name = input("Name: ").title()
    wins = get_int("Wins: ")
    losses = get_int("Losses: ")
    ties = get_int("Ties: ")
    player = Player(name, wins, losses, ties)
    db.add_player(player)    
    print(f"{player.name} was added to database.\n")

def delete_player():
    name = input("Name: ").title()
    db.delete_player(name)
    print(f"{name} was deleted from database.\n")
        
def main():
    db.connect()
    display_title()
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "view":
            display_players()
        elif command == "add":
            add_player()
        elif command == "del":
            delete_player()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
