from abc import ABC, abstractmethod
from typing import Any


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str,
                   targets: list[Any]) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]:
        raise NotImplementedError
