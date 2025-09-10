from dataclasses import dataclass, field
from typing import List

from Card import Card


@dataclass
class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.hand = []