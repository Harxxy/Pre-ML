from deck import Deck
from card import Card

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def value(self):
        total = 0
        aces = 0
        for card in self.cards:
            if card.rank in ('J', 'Q', 'K'):
                total += 10
            elif card.rank == 'A':
                total += 11
                aces += 1
            else:
                total += int(card.rank)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

def is_blackjack(hand):
    return hand.value() == 21

def is_bust(hand):
    return hand.value() > 21