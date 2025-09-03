import random
from Card import RANKS, SUITS, SPECIALS

class Game:
    def __init__(self):
        self.deck = []
        self.shuffled_deck = []

    def init_and_shuffle_deck(self):
        self.deck = [f'{rank} of {suit}' for suit in SUITS for rank in RANKS]
        self.deck += ['Red Joker', 'Black Joker']
        self.deck += SPECIALS  # Add special cards
        self.shuffled_deck = self.deck.copy()
        random.shuffle(self.shuffled_deck)

    def show_deck(self):
        for card in self.shuffled_deck:
            print(card)

if __name__ == "__main__":
    game = Game()
    game.init_and_shuffle_deck()
    game.show_deck()