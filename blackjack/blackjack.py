""" Import Libraries """
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import *
""" ---------------- """

print("Welcome to BlackJack!\n")

deck = DeckOfCards()
deck.shuffle_deck()
deck.change_value("Ace", 11)
deck.change_value("Jack", 10)
deck.change_value("Queen", 10)
deck.change_value("King", 10)

players = Players()
players.add_players(1,10)
players.add_player_manual("Dealer")
players.show_players()

def update_score_and_aces(player):
    while player.score > 21 and player.ace_count > 0:
        player.score -= 10
        player.ace_count -= 1
    return player.score, player.ace_count

def handle_player_turn(player):
    print(f'{player.name}\'s turn:')
    player.show_hand()
    print(f'Current score: {player.score}')
    while player.score < 21:
        hit = input("Would you like a hit? (y/n): ")
        if hit.lower() == 'y':
            card = deck.get_card()
            player.hand.append(card)
            player.score += card.val
            if card.face == "Ace":
                player.ace_count += 1

            # Update score for Aces
            update_score_and_aces(player)
            
            print(f"{player.name} hits - Card added: {card.face} of {card.suit}")
            print(f"New score is: {player.score}")

            # Check for 21
            if player.score == 21:
                print(f"{player.name} hits 21!")
                break
            elif player.score > 21:
                print(f"{player.name} busts!")
                break

        elif hit.lower() == 'n':
            break
        else:
            print("Invalid response. Please respond with 'y' or 'n'")

    print()

def handle_dealer_turn(dealer):
    print(f'{dealer.name}\'s turn:')
    dealer.show_hand()
    print(f'Current score: {dealer.score}')
    while dealer.score < 17:
        card = deck.get_card()
        dealer.hand.append(card)
        dealer.score += card.val
        if card.face == "Ace":
            dealer.ace_count += 1

        # Update score for Aces
        update_score_and_aces(dealer)

        print(f"{dealer.name} hits - Card added: {card.face} of {card.suit}")
        print(f"New score is: {dealer.score}")

        # Check for 21
        if dealer.score == 21:
            print(f"{dealer.name} hits 21!")
        elif dealer.score > 21:
                print(f"{dealer.name} busts!")
                break
    print()

def show_outcomes(dealer):
    print("Round Results:")
    dealer_busts = dealer.score > 21  # Dealer busts

    for player in players.players:
        if player.position is None:
            continue  # Skip the dealer

        print(f'{player.name}\'s final score: {player.score}')
        if player.score > 21:
            print(f"{player.name} busts!")
        elif dealer_busts:
            print(f"{player.name} wins because the dealer busts!")
            player.win_count += 1
        elif dealer.score < player.score <= 21:
            print(f"{player.name} wins with a higher score than the dealer!")
            player.win_count += 1
        elif dealer.score == player.score:
            print(f"{player.name} loses, tying with the dealer.")
        else:
            print(f"{player.name} loses to the dealer.")

    print(f"{dealer.name}'s final score: {dealer.score}")
    print("-- -- -- -- -- -- -- -- -- --")

def declare_overall_winner():
    print("Overall Win Counts:")
    max_wins = max(player.win_count for player in players.players if player.position is not None)
    winners = [player.name for player in players.players if player.win_count == max_wins and player.position is not None]
    
    if winners:
        print(f"Overall Winner(s): {', '.join(winners)} with {max_wins} wins!")
    else:
        print("No winners this round.")

def play_blackjack():
    print('Welcome to BlackJack!\n')
    
    playagain = 'y'
    while playagain.lower() == 'y':
        # Initialize hands and scores
        for player in players.players:
            player.hand = []
            player.score = 0
            player.ace_count = 0

        # Deal 2 cards to each player
        for player in players.players:
            player.hand.append(deck.get_card())
            player.hand.append(deck.get_card())
        
        # Update player scores and ace counts
        for player in players.players:
            player.score = sum(card.val for card in player.hand)
            player.ace_count = sum(1 for card in player.hand if card.face == "Ace")
        
        # Adjust scores for Aces initially
        for player in players.players:
            update_score_and_aces(player)
        
        # Handle turns for players and dealer
        for player in players.players:
            if player.position is not None:  # Player turn
                handle_player_turn(player)
            else:  # Dealer turn
                handle_dealer_turn(player)
        
        # Show outcomes
        dealer = [player for player in players.players if player.position is None][0]
        show_outcomes(dealer)
        
        playagain = input('Play again? (y/n): ')

        if playagain.lower() == 'n':
            declare_overall_winner()


play_blackjack()