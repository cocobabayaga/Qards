import random
from Card import RANKS, SUITS, SPECIALS

class Game:
    def __init__(self):
        self.deck = []
        self.shuffled_deck = []

    def init_and_shuffle_deck(self, num_decks=2):
        self.deck = []
        for _ in range(num_decks):
            self.deck += [f'{rank} of {suit}' for suit in SUITS for rank in RANKS]

        #self.deck += ['Red Joker', 'Black Joker']
        self.deck += SPECIALS  # Add special cards
        self.shuffled_deck = self.deck.copy()
        random.shuffle(self.shuffled_deck)

    def show_deck(self):
        for card in self.shuffled_deck:
            print(card)

    def deal_cards(self, num_players=4, cards_per_player=8):
        players_hands = [[] for _ in range(num_players)]
        for _ in range(cards_per_player):
            for player in players_hands:
                if self.shuffled_deck:
                    player.append(self.shuffled_deck.pop(0))
        return players_hands



if __name__ == "__main__":
    game = Game()
    game.init_and_shuffle_deck()
    hands = game.deal_cards()
    for i, hand in enumerate(hands, 1):
        print(f"Player {i} hand ({len(hand)} cards): {hand}")
    game.show_deck()