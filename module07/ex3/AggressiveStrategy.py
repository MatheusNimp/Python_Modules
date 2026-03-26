from typing import Any

from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list[Any],
                     battlefield: list[Any]) -> dict[str, Any]:
        sorted_hand = sorted(hand, key=lambda card: card.cost)
        mana_budget = 5
        cards_played: list[str] = []
        mana_used = 0
        damage_dealt = 0

        for card in sorted_hand:
            if mana_used + card.cost > mana_budget:
                continue
            cards_played.append(card.name)
            mana_used += card.cost
            if getattr(card, "card_type", "") == "Creature":
                damage_dealt += getattr(card, "attack", 0)
                battlefield.append(card)
            elif isinstance(card, SpellCard):
                damage_dealt += 3

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        if "Enemy Player" in available_targets:
            remaining = [
                target for target in available_targets
                if target != "Enemy Player"]
            return ["Enemy Player", *remaining]
        return available_targets
