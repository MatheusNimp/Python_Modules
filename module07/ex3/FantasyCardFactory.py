from typing import Any

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.registry = {
            "creatures": {
                "dragon": lambda: CreatureCard(
                    "Fire Dragon", 5, "Legendary", 5, 5),
                "goblin": lambda: CreatureCard(
                    "Goblin Warrior", 2, "Common", 5, 2),
            },
            "spells": {
                "fireball": lambda: SpellCard(
                    "Lightning Bolt", 3, "Rare", "damage"),
            },
            "artifacts": {
                "mana_ring": lambda: ArtifactCard(
                    "Mana Ring", 2, "Rare", 3, "+1 mana per turn"),
            },
        }

    def create_creature(self, name_or_power: str | int | None = None):
        if (isinstance(name_or_power, str)
           and name_or_power.lower() in self.registry["creatures"]):
            return self.registry["creatures"][name_or_power.lower()]()
        return self.registry["creatures"]["dragon"]()

    def create_spell(self, name_or_power: str | int | None = None):
        if (isinstance(name_or_power, str)
           and name_or_power.lower() in self.registry["spells"]):
            return self.registry["spells"][name_or_power.lower()]()
        return self.registry["spells"]["fireball"]()

    def create_artifact(self, name_or_power: str | int | None = None):
        if (isinstance(name_or_power, str)
           and name_or_power.lower() in self.registry["artifacts"]):
            return self.registry["artifacts"][name_or_power.lower()]()
        return self.registry["artifacts"]["mana_ring"]()

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        cards = [self.create_creature("dragon"),
                 self.create_creature("goblin"), self.create_spell("fireball")]
        if size > 3:
            cards.extend(self.create_artifact(
                "mana_ring") for _ in range(size - 3))
        return {"theme": "fantasy", "size": size, "cards": cards[:size]}

    def get_supported_types(self) -> dict[str, Any]:
        return {key: list(values.keys())
                for key, values in self.registry.items()}
