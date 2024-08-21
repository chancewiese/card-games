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
# players.add_players(1,10)
players.add_player_manual("Chance", 1)
players.add_player_manual("Dave", 2)
players.add_player_manual("Traci", 3)
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


# playagain = 'y'     # This runs the code again if they choose to
# uwincount = 0
# dwincount = 0
# while playagain == 'y':
    
#     deck = DeckOfCards()
#     deck.shuffle_deck()
#     print()
    
#     # deals two cards to the user
#     ucard = deck.get_card()
#     ucard2 = deck.get_card()
#     print()
#     print("Card number 1 is: "+ucard.face+" of "+ucard.suit)
#     print("Card number 2 is: "+ucard2.face+" of "+ucard2.suit)
#     ucardnumber = 2
    
#     # calculates the user's hand score to begin
#     uscore = 0
#     uscore += ucard.val
#     uscore += ucard2.val
#     print("Your score is:", uscore)
#     print()
    
#     # calculates the user's number of aces to begin
#     uace = 0
#     if ucard.face == "Ace":
#         uace += 1
#     if ucard2.face == "Ace":
#         uace += 1
    
#     # deals two cards to the dealer
#     dcard = deck.get_card()
#     dcard2 = deck.get_card()
#     dcardnumber = 2
    
#     # calculates the dealer's hand score to begin
#     dscore = 0
#     dscore += dcard.val
#     dscore += dcard2.val
    
#     # calculates the dealer's number of aces to begin
#     dace = 0
#     if dcard.face == "Ace":
#         dace += 1
#     if dcard2.face == "Ace":
#         dace += 1
    
#     # while hit is 'y' and score <= 21, ask the user if they want to hit
#     hit = 'y'
#     while hit == 'y' and uscore < 21:
#         hit = input("Would you like a hit?(y/n): ")
#         print()
#         if hit == 'y':      #if they want a hit, give them another card
#             ucard_new = deck.get_card()
#             ucardnumber += 1        #keep track of how many cards they have
#             print("Card number",ucardnumber,"is: "+ucard_new.face+" of "+ucard_new.suit)
#             if ucard_new.face == "Ace": #if the new card is an ace, add it to the count
#                 uace += 1
#             uscore += ucard_new.val     #adjust total score
#             if uscore > 21 and uace > 0:        #if they have an ace and busted, drop them 10 and remove their ace from the count
#                 uscore -= 10
#                 uace -= 1
#             print("Your new score is:", uscore)
#             print()
#         elif hit == 'n':        #if they don't want to hit, jump out of loop
#             break
#         else:       #if they didn't answer y or n, then try again
#             print("Invalid response. Please respond with 'y' or 'n'")
#             hit = 'y' #resets the if loop to see if they want to hit
    
#     if uscore > 21: #tell them if they busted
#         dwincount += 1
#         print("User busted, you lose!")
        
#     if uscore <=21:     #if they didn't bust, run the dealers cards
#         print("Dealer card number 1 is: "+dcard.face+" of "+dcard.suit)     #reveal dealer cards
#         print("Dealer card number 2 is: "+dcard2.face+" of "+dcard2.suit)
#         while dscore < 17:  #if they have less than 17, hit
#             dcard_new = deck.get_card()
#             dcardnumber += 1        #keep track of how many cards are hit
#             print("Dealer hits, card number",dcardnumber,"is: "+dcard_new.face+" of "+dcard_new.suit)
#             if dcard_new.face == "Ace": #if the new card is an ace, add it to the count
#                 dace += 1
#             dscore += dcard_new.val
#             if dscore > 21 and dace > 0: #if the dealer busts and has an ace, subtract 10 and remove an ace
#                 dscore -= 10
#                 dace -= 1
#         print("Dealer score is:", dscore)   #reveal dealer score after hits
#         print()
        
#         print("User Score:", uscore)    #reveal final scores
#         print("Dealer Score:", dscore)
#     if dscore > 21:     #if dealer busts, tell user they won
#         uwincount += 1
#         print("The dealer busted, you win!")
#     if dscore >= uscore and dscore <= 21:   #if dealer is less than or equal to 21 and greater than or equal to the user, dealer wins
#         dwincount += 1
#         print("The dealer wins with a score of %d!" % (dscore))
#     if uscore > dscore and uscore <= 21:    #if user is greater than dealer and less than or equal to 21, the user wins. I could've left this with an else but it helps me understand the logic
#         uwincount += 1
#         print("The user wins with a score of %d!" % (uscore))
#     playagain = input("\nWould you like to play again?(y/n): ") #if they play again, it'll run through the loop
    
    
    
#     # I added this after but it counts the amount of wins that they both have and announces a final winner
# print("\n\nUser win count:",uwincount)
# print("Dealer win count:",dwincount)
# if uwincount > dwincount:
#     print("You are the overall winner!")
# elif dwincount > uwincount:
#     print("The dealer is the overall winner!")
# else:
#     print("It's a tie!")
    
    
# print("\n\nThanks for playing!")


# # ! NEW

# from DeckOfCards import DeckOfCards

# print("Welcome to BlackJack!\n")

# def get_initial_score(cards):
#     score = sum(card.val for card in cards)
#     aces = sum(1 for card in cards if card.face == "Ace")
#     return score, aces

# def deal_cards(deck, num_cards):
#     return [deck.get_card() for _ in range(num_cards)]

# def calculate_score(cards, aces):
#     score = sum(card.val for card in cards)
#     while score > 21 and aces:
#         score -= 10
#         aces -= 1
#     return score

# def play_game():
#     uwincount = 0
#     dwincount = 0

    # playagain = 'y'
    # while playagain.lower() == 'y':
#         deck = DeckOfCards()
        
#         ucards = deal_cards(deck, 2)
#         dcards = deal_cards(deck, 2)
        
#         uscore, uace = get_initial_score(ucards)
#         dscore, dace = get_initial_score(dcards)
        
#         while uscore < 21:
#             hit = input("Would you like a hit? (y/n): ")
#             if hit.lower() == 'y':
#                 ucard_new = deck.get_card()
#                 ucards.append(ucard_new)
#                 uscore = calculate_score(ucards, uace)
#                 print(f"Card number {len(ucards)} is: {ucard_new.face} of {ucard_new.suit}")
#                 print(f"Your new score is: {uscore}")
#             elif hit.lower() == 'n':
#                 break
#             else:
#                 print("Invalid response. Please respond with 'y' or 'n'")

#         if uscore > 21:
#             dwincount += 1
#             print("User busted, you lose!")
#         else:
#             while dscore < 17:
#                 dcard_new = deck.get_card()
#                 dcards.append(dcard_new)
#                 dscore = calculate_score(dcards, dace)
#                 print(f"Dealer hits, card number {len(dcards)} is: {dcard_new.face} of {dcard_new.suit}")

#             print(f"Dealer score is: {dscore}")
#             print(f"User Score: {uscore}")
            
#             if dscore > 21:
#                 uwincount += 1
#                 print("The dealer busted, you win!")
#             elif dscore >= uscore:
#                 dwincount += 1
#                 print("The dealer wins with a score of %d!" % dscore)
#             else:
#                 uwincount += 1
#                 print("The user wins with a score of %d!" % uscore)

#         playagain = input("\nWould you like to play again? (y/n): ")

#     return uwincount, dwincount

# uwincount, dwincount = play_game()

# print("\nUser win count:", uwincount)
# print("Dealer win count:", dwincount)

# if uwincount > dwincount:
#     print("You are the overall winner!")
# elif dwincount > uwincount:
#     print("The dealer is the overall winner!")
# else:
#     print("It's a tie!")

# print("\nThanks for playing!")
