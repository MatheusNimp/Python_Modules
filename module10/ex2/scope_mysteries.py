"""Memory Depths exercises.

This module demonstrates closures, lexical scoping, and nonlocal state.
"""

from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    """Return an independent counter closure."""
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Return a closure that accumulates spell power."""
    total_power = initial_power

    def add_power(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Return a closure that applies one enchantment type to items."""

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return private memory store and recall closures."""
    memories: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memories[key] = value

    def recall(key: str) -> object:
        return memories.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    """Demonstrate closure-based state management."""
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("Testing memory vault...")
    vault = memory_vault()
    store = vault["store"]
    recall = vault["recall"]
    store("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")


if __name__ == "__main__":
    main()
