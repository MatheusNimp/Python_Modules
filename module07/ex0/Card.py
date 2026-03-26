from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"
    TOURNAMENT = "Tournament"


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not name.strip():
            raise ValueError("name must not be empty")
        if cost < 0:
            raise ValueError("cost must be non-negative")
        self.name = name
        self.cost = cost
        self.rarity = self._normalize_rarity(rarity)
        self.card_type = self._infer_card_type()

    @staticmethod
    def _normalize_rarity(rarity: str) -> str:
        try:
            return Rarity(rarity.title()).value
        except ValueError:
            return rarity

    def _infer_card_type(self) -> str:
        return self.__class__.__name__.replace("Card", "") or "Card"

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.card_type,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

    def __repr__(self) -> str:
        return f"{self.name} ({self.cost})"
