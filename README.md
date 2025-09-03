# Qards

**Developed by:**  
4 students (Physics & Computer Science)  
Quantum Experience Course, Joint Degree AQT AUAS, Fontys, THUAS, Saxion

MAQT Challenge for the Quantum Experience Project

## Development Requirements

To develop and run Qards, you need:
- An IDE (such as PyCharm)
- Python 3.x
- The `pygame` package (version 2.6.1)

Install pygame with:
```pip install pygame==2.6.1```

## Game Concept

Qards is a digital card game inspired by the classic "Shithead" (Pesten), reimagined with quantum mechanics concepts.

## Quantum Rules

- **Quantum Teleportation:**  
  If a player has two cards of the same number, they may (on their turn) give one to the player opposite and draw a random card from that player's deck.

- **Entanglement:**  
  Drawing the entanglement card adds it to your deck, entangled with another card. You may give the entangled card to a random opponent. Only the giver and receiver know the card.

- **Cryostat:**  
  The cryostat card freezes the next player's turn; they must skip their move.

- **Superfluid:**  
  Playing the superfluid transition card grants the player an extra turn.

- **Spin:**  
  Drawing the spin card triggers a random choice (by the computer):  
  - Plus: Draw 2 extra cards  
  - Minus: Discard 2 cards

- **Superconduction:**  
  Drawing the superconduction card allows the player to discard a non-power card to the pile. The next player must draw that many cards from the pile.

### Extra: Normalisation

The probability of drawing a "bully" card changes based on the number of cards in a player's deck, affecting gameplay dynamics.