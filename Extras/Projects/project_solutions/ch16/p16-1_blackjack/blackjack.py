#!/usr/bin/env python3

import random

from objects import Card, Deck, Hand

def main():
    print("Blackjack")
    print()

    again = "y"
    while again.lower() == "y":
        deck = Deck()
        deck.shuffle()

        dealer_hand = Hand()
        player_hand = Hand()

        # get player and dealer hands
        player_hand.addCard(deck.dealCard())
        player_hand.addCard(deck.dealCard())
        dealer_hand.addCard(deck.dealCard())
        show_card = deck.dealCard()  # store dealer show card in variable
        dealer_hand.addCard(show_card)
        
        # display cards
        display_card(show_card, "DEALER'S SHOW CARD: ")
        display_cards(player_hand, "YOUR CARDS: ")       

        # if player or dealer has blackjack, display dealer's cards and
        # move to determine winner. Otherwise, player and dealer draw
        # as needed
        if dealer_hand.isBlackjack or player_hand.isBlackjack:
            display_cards(dealer_hand, "DEALER'S CARDS: ")
        else:
            player_hand = play(deck, player_hand)
        
            if not player_hand.isBusted:
                while dealer_hand.points < 17:        
                    dealer_hand.addCard(deck.dealCard())
                
            display_cards(dealer_hand, "DEALER'S CARDS: ")

        print(f"YOUR POINTS:     {player_hand.points}")    
        print(f"DEALER'S POINTS: {dealer_hand.points}")
        print()

        # determine winner
        if player_hand.isBusted:    
            print("Sorry. You busted. You lose.")
        elif dealer_hand.isBusted:
            print("Yay! The dealer busted. You win!")
        else:        
            if player_hand.isBlackjack:
                if dealer_hand.isBlackjack:
                    print("Dang, dealer has blackjack too. You push.")
                else:
                    print("Blackjack! You win!")
            elif player_hand.points > dealer_hand.points:    
                print("Hooray! You win!")
            elif player_hand.points == dealer_hand.points:    
                print("You push.")
            elif player_hand.points < dealer_hand.points:    
                print("Sorry. You lose.")
            else:
                print("I am not sure what happened.")
        print()

        again = input("Play again? (y/n): ").lower()
        print()
        
    print("Come back soon!")

def play(deck, player_hand):
    while True:
        choice = input("Hit or stand? (h/s): ").lower()
        print()

        if choice == "h":
            player_hand.addCard(deck.dealCard())
            display_cards(player_hand, "YOUR CARDS: ")
            if player_hand.points >= 21:
                break
        elif choice == "s":
            break
        else:
            print("Not a valid choice. Try again.")
    return player_hand

def display_cards(hand, title):
    print(title.upper())
    for card in hand:
        print(f"   {card}")
    print()

def display_card(card, title):
    print(title.upper())
    print(f"   {card}")
    print()


if __name__ == "__main__":
    main()
