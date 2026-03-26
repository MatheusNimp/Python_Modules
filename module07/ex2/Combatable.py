from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Any) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]:
        raise NotImplementedError
