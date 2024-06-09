import random      # Random for shuffling


class Card(): 
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.val = value
        
    def __str__(self):
        return self.face + " of " + self.suit + ", value: " + str(self.val)


class DeckOfCards(): 
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.faces = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.play_idx = 0
        
        for suit in self.suits:
            i = 0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[i], self.values[i]))
                
                
    def shuffle_deck(self):     # Shuffle deck
        random.shuffle(self.deck)
        self.play_idx = 0
        
    def print_deck(self):       # Prints deck
        for card in self.deck:
            print(card.face, "of", card.suit, end=", ")
        print("---")
        
    def get_card(self):     # Gets the top card from the deck
        self.play_idx += 1
        return self.deck[self.play_idx - 1]