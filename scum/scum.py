exec(open('setup.py').read())

from DeckOfCards import *
from Players import *


##################################################

# Functions
def prepare_deck():
    deck = DeckOfCards()            # Set deck initially
    deck.change_value("Ace", 14)    # Change value of aces
    deck.add_jokers(1, 100)         # Add joker
    return deck

def find_players():
    players = []
    player_count = 1
    find_player_check = True
    # Need 2-8 players for Scum

    while find_player_check == True:
        player_name = input(f"Player {player_count} Name ('s' to stop adding): ")
        
        if player_name.lower() == 's':
            if len(players) < 2:
                print(f'Need {2 - len(players)} more players!')
            else:
                find_player_check = False
        else:
            players.append(player_name)
            player_count += 1

        if len(players) == 8:
            print("That's all 8 players!")
            find_player_check = False
    return players


deck = prepare_deck()


players = Players()
players.add_players(2,8)
players.set_positions()
players.deal_cards(deck)

players.show_players()