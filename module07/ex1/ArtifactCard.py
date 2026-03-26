from typing import Any

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("durability must be positive")
        self.durability = durability
        self.effect = effect
        self.card_type = "Artifact"

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        artifacts = game_state.setdefault("artifacts", [])
        artifacts.append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict[str, Any]:
        return {
            "artifact": self.name,
            "durability": self.durability,
            "ability": self.effect,
            "activated": True,
        }
