from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana_pool: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.mana_pool = mana_pool
        self.card_type = "Elite"

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        battlefield = game_state.setdefault("battlefield", [])
        battlefield.append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite unit deployed with hybrid abilities",
        }

    def attack(self, target: Any) -> dict[str, Any]:
        return {
            "attacker": self.name,
            "target": getattr(target, "name", str(target)),
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        blocked = min(3, incoming_damage)
        taken = max(0, incoming_damage - blocked)
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {"attack": self.attack_power, "health": self.health}

    def cast_spell(self, spell_name: str,
                   targets: list[Any]) -> dict[str, Any]:
        mana_used = min(4, self.mana_pool)
        self.mana_pool -= mana_used
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [getattr(target, "name",
                                str(target)) for target in targets],
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> dict[str, Any]:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict[str, Any]:
        return {"mana_pool": self.mana_pool, "spell_power": self.attack_power}
