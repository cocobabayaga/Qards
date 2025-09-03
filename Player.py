from dataclasses import dataclass, field
from typing import List

from Card import Card


@dataclass
class Player:
    id: int
    name: str
    hand: List[Card] = field(default_factory=list)