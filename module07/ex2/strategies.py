from abc import ABC, abstractmethod
from ex0.abstractions import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    name: str

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass

    def _ensure_valid(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            message = (
                f"Invalid Creature '{creature.name}' "
                f"for this {self.name.lower()} strategy"
            )
            raise InvalidStrategyError(message)


class NormalStrategy(BattleStrategy):
    name = "Normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        self._ensure_valid(creature)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    name = "Aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        self._ensure_valid(creature)
        transforming_creature = creature
        if not isinstance(transforming_creature, TransformCapability):
            raise InvalidStrategyError("Creature lost transform capability")
        return [
            transforming_creature.transform(),
            transforming_creature.attack(),
            transforming_creature.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    name = "Defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        self._ensure_valid(creature)
        healing_creature = creature
        if not isinstance(healing_creature, HealCapability):
            raise InvalidStrategyError("Creature lost heal capability")
        return [
            healing_creature.attack(),
            healing_creature.heal(),
        ]
