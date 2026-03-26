from abc import ABC, abstractmethod
from typing import Any


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list[Any],
                     battlefield: list[Any]) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_strategy_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def prioritize_targets(self, available_targets: list[Any]) -> list[Any]:
        raise NotImplementedError
