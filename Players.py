class Player(): 
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"Player: {self.name}"

class Players: 
    def __init__(self):
        self.players = []

    def add_players(self, min_players, max_players):
        count = 1
        while True:
            name = input(f"Player {count} Name ('s' to stop adding): ")
            if name.lower() == 's':
                if len(self.players) < min_players:
                    print(f'Need at least {min_players - len(self.players)} more players!')
                else:
                    break
            else:
                self.players.append(Player(name))
                count += 1
                if len(self.players) == max_players:
                    print(f"Reached maximum of {max_players} players!")
                    break
        return self.players

    def set_positions(self):
        for i, player in enumerate(self.players, start=1):
            player.position = i

    def deal_cards(self, deck):
        while len(deck.deck) > 0:
            for player in self.players:
                if len(deck.deck) > 0:
                    player.hand.append(deck.deck.pop(0))

    def show_players(self):
        for player in self.players:
            print(f"Position: {player.position}, Name: {player.name}")
            print("Hand:")
            for card in player.hand:
                print(card)  # This will call the __str__ method of the Card class
            print("-- -- -- -- -- -- -- -- -- --")