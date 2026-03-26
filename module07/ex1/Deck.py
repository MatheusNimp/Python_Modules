import random
from typing import Any

from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for index, card in enumerate(self.cards):
            if card.name == card_name:
                del self.cards[index]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict[str, Any]:
        total_cards = len(self.cards)
        total_cost = sum(card.cost for card in self.cards)
        return {
            "total_cards": total_cards,
            "creatures": sum(card.card_type == "Creature"
                             for card in self.cards),
            "spells": sum(card.card_type == "Spell" for card in self.cards),
            "artifacts": sum(card.card_type == "Artifact"
                             for card in self.cards),
            "avg_cost": round(total_cost / total_cards, 2)
            if total_cards else 0.0,
        }
