"""Ancient Library exercises.

This module demonstrates functools.reduce, functools.partial,
functools.lru_cache, and functools.singledispatch.
"""

import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using the requested operation."""
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) -> dict[str, Callable[[str], str]]:
    """Create specialized elemental enchantments with functools.partial."""
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "ice": functools.partial(base_enchantment, 50, "ice"),
        "lightning": functools.partial(base_enchantment, 50, "lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using cached recursion."""
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create and return a singledispatch spell handler."""

    @functools.singledispatch
    def dispatch(spell_data: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell_data: int) -> str:
        return f"Damage spell: {spell_data} damage"

    @dispatch.register
    def _(spell_data: str) -> str:
        return f"Enchantment: {spell_data}"

    @dispatch.register
    def _(spell_data: list) -> str:
        return f"Multi-cast: {len(spell_data)} spells"

    return dispatch


def base_enchantment(power: int, element: str, target: str) -> str:
    """Demo base enchantment function for partial application."""
    return f"{target} receives {element} enchantment with {power} power"


def main() -> None:
    """Demonstrate functools helpers."""
    spell_powers = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    print("Testing partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire"]("Sword"))

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "heal"]))
    print(dispatcher({"unknown": True}))


if __name__ == "__main__":
    main()
