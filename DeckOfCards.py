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
        self.build_deck()

    def build_deck(self):
        self.deck = []
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

    def change_value(self, face, new_value):  # Change value of a specific face
        for card in self.deck:
            if card.face == face:
                card.val = new_value

    def modify_suit(self, suit, action):  # Add or remove suit
        if action == 'add' and suit not in self.suits:
            self.suits.append(suit)
        elif action == 'remove' and suit in self.suits:
            self.suits.remove(suit)
        else:
            raise ValueError("Issue with modify_suit")
        self.build_deck()

    def modify_face(self, face, value=None, action='add'):  # Add or remove face
        if action == 'add' and face not in self.faces:
            if value is None:
                raise ValueError("Value must be provided when adding a new face.")
            self.faces.append(face)
            self.values.append(value)
        elif action == 'remove' and face in self.faces:
            index = self.faces.index(face)
            self.faces.pop(index)
            self.values.pop(index)
        else:
            raise ValueError("Issue with modify_face")
        self.build_deck()

    def count_cards(self):      # Count the number of cards in the deck
        return len(self.deck)
    
    def add_jokers(self, num_jokers, value):  # Add jokers to the deck
        for _ in range(num_jokers):
            self.deck.append(Card("Jokers", "Joker", value))

    def print_deck_clean(self):
        print("-- -- -- -- -- -- -- -- -- --")
        suits_dict = {}
        for card in self.deck:
            if card.suit not in suits_dict:
                suits_dict[card.suit] = []
            suits_dict[card.suit].append(card)

        for suit, cards in suits_dict.items():
            print(f"{suit}:")
            # Organize cards within each suit by value
            cards.sort(key=lambda x: x.val)
            for card in cards:
                print(card)
            print("-- -- -- -- -- -- -- -- -- --")