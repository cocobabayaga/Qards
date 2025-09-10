import random
from Card import RANKS, SUITS, SPECIALS
from Player import Player

class Game:
    def __init__(self):
        self.players = []
        self.deck = []
        self.shuffled_deck = []

    def init_and_shuffle_deck(self, num_decks=2):
        self.deck = []
        for _ in range(num_decks):
            self.deck += [f'{rank} of {suit}' for suit in SUITS for rank in RANKS]

        self.deck += SPECIALS
        self.shuffled_deck = self.deck.copy() #TODO: shuffle the already init deck when playing multiple rounds
        random.shuffle(self.shuffled_deck)

    def show_deck(self):
        for card in self.shuffled_deck:
            print(card)

    def deal_cards(self, num_players=4, cards_per_player=8):
        self.players = [Player(id + 1) for id in range(num_players)]
        for _ in range(cards_per_player):
            for player in self.players:
                if self.shuffled_deck:
                    player.hand.append(self.shuffled_deck.pop(0))
        return self.players

    def decide_starting_player(self, players):
        return random.choice(players)


if __name__ == "__main__":
    game = Game()
    game.init_and_shuffle_deck()
    hands = game.deal_cards()
    for i, player in enumerate(hands, 1):
        print(f"Player {i} hand ({len(player.hand)} cards): {player.hand}")

    game.show_deck()