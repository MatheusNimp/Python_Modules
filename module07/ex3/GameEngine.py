from typing import Any

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand: list[Any] = []
        self.battlefield: list[Any] = []
        self.turns_simulated = 0
        self.total_damage = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            factory.create_creature("dragon"),
            factory.create_creature("goblin"),
            factory.create_spell("fireball"),
        ]

    def simulate_turn(self) -> dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise ValueError("engine must be configured before simulation")
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += int(result.get("damage_dealt", 0))
        return result

    def get_engine_status(self) -> dict[str, Any]:
        strategy_name = (
            self.strategy.get_strategy_name() if self.strategy else None)
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": len(self.hand),
        }
