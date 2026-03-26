from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        rating: int = 1200,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.attack_power = attack_power
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = rating
        self.card_type = "Tournament"

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament combatant enters arena",
        }

    def attack(self, target: Any) -> dict[str, Any]:
        return {
            "attacker": self.card_id,
            "target": getattr(target, "card_id", str(target)),
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        blocked = min(2, incoming_damage)
        taken = max(0, incoming_damage - blocked)
        self.health -= taken
        return {
            "defender": self.card_id,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict[str, Any]:
        return {"attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("wins must be non-negative")
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("losses must be non-negative")
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "id": self.card_id,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        return {
            "card_id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
        }
