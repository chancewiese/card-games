exec(open('setup.py').read())

from DeckOfCards import *
from Players import *


##################################################

# Functions
def prepare_players():
    players = Players()
    players.add_players(2,10)
    num_players = players.count_players()
    return players, num_players

def prepare_deck(num_players):
    deck = DeckOfCards()
    deck.add_decks(calculate_decks_needed(num_players, 5))
    deck.change_value("Ace", 14)    # Change value of aces
    deck.add_jokers(1, 100)         # Add joker
    deck.shuffle_deck()
    return deck

def play_turn(prevturn_card_count, prevturn_card_score):
    print()







def play():
    # Starting values and settings
    players, num_players = prepare_players()    # Set players & find number of players
    deck = prepare_deck(num_players)            # Set deck
    num_rounds = num_players

    for round in range(1,num_rounds+1):
        players.deal_cards(deck)                    # Deal cards

        print(f"Round {round}:")
        for player in players.players:
            player.show_hand()

        while True:
            discard_pile = []
            remaining_players = [player for player in players.players if player.hand]  # Players with cards
            if len(remaining_players) == 1:             # End game if only one player left with cards
                print(f"{remaining_players[0].name} wins the round!")
                break  

            for player in remaining_players:
                print(f"\n{player.name}'s turn:")
                player.show_hand()
                play_cards = input("Enter the cards you want to play (comma-separated): ").split(',')
                # Convert input to card objects from player's hand
                cards_to_play = [card for card in player.hand if str(card) in play_cards]

                # Play the selected cards
                for card in cards_to_play:
                    player.hand.remove(card)
                    discard_pile.append(card)
                cards_played_count = len(cards_to_play)




play()