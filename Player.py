from dataclasses import dataclass
from typing import List

from Card import Card


@dataclass
class Player:
    idx: int
    name: str
    hand: List[Card] = field(default_factory=list)