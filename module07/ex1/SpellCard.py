from typing import Any

from ex0.Card import Card


class SpellCard(Card):
    VALID_EFFECTS = {"damage", "heal", "buff", "debuff"}

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        normalized = effect_type.lower()
        if normalized not in self.VALID_EFFECTS:
            raise ValueError("invalid effect_type")
        self.effect_type = normalized
        self.card_type = "Spell"

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        graveyard = game_state.setdefault("graveyard", [])
        graveyard.append(self.name)
        effects = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to ally",
            "buff": "Grant +2 attack this turn",
            "debuff": "Reduce enemy power by 2",
        }
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effects[self.effect_type],
        }

    def resolve_effect(self, targets: list[Any]) -> dict[str, Any]:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": [getattr(target, "name",
                                str(target)) for target in targets],
            "resolved": True,
        }
