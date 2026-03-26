from abc import ABC, abstractmethod
from typing import Any


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_rank_info(self) -> dict[str, Any]:
        raise NotImplementedError
