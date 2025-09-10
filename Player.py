from dataclasses import dataclass, field
from typing import List

from Card import Card


@dataclass
class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []
