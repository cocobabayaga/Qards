from dataclasses import dataclass
from typing import Optional

CARD_W, CARD_H = 80, 110
# Special names
CRYOSTAT = "Cryostat"
SUPERFLUID = "Superfluid"
SPIN = "Spin"
SUPERCONDUCTION = "Superconduction"
ENTANGLEMENT = "Entanglement"

SPECIALS = [CRYOSTAT, SUPERFLUID, SPIN, SUPERCONDUCTION, ENTANGLEMENT]

# Normal ranks and suits
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["♠", "♥", "♦", "♣"]

# Value map for superconduction
RANK_VALUE = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Joker": 11,
    "Queen": 12,
    "King": 13,
}

# Normalization parameters
BASE_SPECIAL_P = 0.15
ADJ_PER_CARD = 0.03
MIN_SPECIAL_P = 0.05
MAX_SPECIAL_P = 0.50

@dataclass
class Card:
    kind: str  # 'NORMAL' or 'SPECIAL'
    rank: Optional[str] = None  # for normal
    suit: Optional[str] = None
    special: Optional[str] = None  # for special
    # For entanglement secrecy on a card that was sent to an opponent
    private_known_for: Optional[int] = None  # player index that can see this card fully
