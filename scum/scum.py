exec(open('setup.py').read())

from DeckOfCards import *
from Players import *


##################################################

# Functions
def prepare_players():
    players = Players()
    players.add_players(2,10)
    players.set_positions()
    return players

def prepare_deck(num_players):
    deck = DeckOfCards()
    deck.add_decks(calculate_decks_needed(num_players, 5))
    deck.change_value("Ace", 14)    # Change value of aces
    deck.add_jokers(1, 100)         # Add joker
    return deck

# Starting values and settings
players = prepare_players()             # Set players
num_players = players.count_players()   # Find number of players
deck = prepare_deck(num_players)        # Set deck


players.deal_cards(deck)
players.show_players()