exec(open('setup.py').read())

from DeckOfCards import *


##################################################

deck = DeckOfCards()
deck.shuffle_deck()

play = 'y'

players = []
print('Need 2-8 players for Scum.')
findplayercount = True
playercount = 1
while findplayercount == True:
    players.append(input(f"Player {playercount} Name ('s' to stop adding): "))
    playercount += 1
    if len(players) < 3 and players[-1] == 's':
        print('Need {playercount} more players!')
        players.pop()
        playercount -= 1
    if len(players) > 2 and players[-1] == 's':
        players.pop()
        findplayercount = False
    if len(players) == 8 and players[-1] != 's':
        print("That's all 8 players!")
        findplayercount = False

print(players)
print(len(players))
cardsperplayer = 52/len(players)
print(cardsperplayer)

# while play == 'y':
    