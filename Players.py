class Player(): 
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.position = None
        self.win_count = 0

    def __str__(self):
        return f"Player: {self.name}"
    
    def sort_hand(self):
        self.hand.sort(key=lambda card: card.val)

    def show_hand(self):
        for card in self.hand:
            print(card)

class Players: 
    def __init__(self):
        self.players = []

    def add_players(self, min_players, max_players):
        players = []
        count = 1
        while True:
            name = input(f"Player {count} Name ('s' to stop adding): ").strip()
            if name.lower() == 's':
                if len(players) < min_players:
                    print(f'Need at least {min_players - len(players)} more players!')
                else:
                    break
            else:
                player = Player(name)
                player.position = count
                players.append(player)
                count += 1
                if len(players) == max_players:
                    print(f"Reached maximum of {max_players} players!")
                    break
        print()
        self.players = players  # Update the players list in the class
        return self.players
    
    def add_player_manual(self, name, position=None):
        player = Player(name)
        player.position = position
        self.players.append(player)
    
    def count_players(self):
        return len(self.players)

    def deal_cards(self, deck):
        while len(deck.deck) > 0:
            for player in self.players:
                if len(deck.deck) > 0:
                    player.hand.append(deck.deck.pop(0))
        for player in self.players:         # Sort each player's hand after dealing
            player.sort_hand()

    def show_players(self):
        for player in self.players:
            print(f"Position: {player.position}, Name: {player.name}")
            print("Hand:")
            for card in player.hand:
                print(card)  # This will call the __str__ method of the Card class
            print("-- -- -- -- -- -- -- -- -- --")