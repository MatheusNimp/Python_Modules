from collections.abc import Callable

Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell_combiner(
    spell1: Spell,
    spell2: Spell,
) -> Callable[[str, int], tuple[str, str]]:
    """Return a spell that casts two spells with the same arguments."""
    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell_combiner expects callable spells")

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        first_result = spell1(target, power)
        second_result = spell2(target, power)
        return (first_result, second_result)

    return combined_spell


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    """Return a spell that multiplies power before casting."""
    if not callable(base_spell):
        raise TypeError("power_amplifier expects a callable spell")

    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Condition, spell: Spell) -> Spell:
    """Return a spell that casts only when condition returns True."""
    if not callable(condition) or not callable(spell):
        raise TypeError("conditional_caster expects callables")

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    """Return a spell that casts every spell in order."""
    for spell in spells:
        if not callable(spell):
            raise TypeError("spell_sequence expects only callable spells")

    def sequence_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_spell


def fireball(target: str, power: int) -> str:
    """Simple demo spell."""
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    """Simple demo spell."""
    return f"Heals {target}"


def lightning(target: str, power: int) -> str:
    """Simple demo spell that displays its power."""
    return f"Lightning strikes {target} with {power} power"


def main() -> None:
    """Demonstrate higher-order spell modifiers."""
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined("Dragon", 10)
    print(f"Combined spell result: {', '.join(combined_result)}")

    print("Testing power amplifier...")
    amplified = power_amplifier(lightning, 3)
    print("Original: 10, Amplified: 30")
    print(amplified("Dragon", 10))

    print("Testing conditional caster...")
    high_power_fireball = conditional_caster(
        lambda target, power: power >= 20,
        fireball,
    )
    print(high_power_fireball("Goblin", 5))
    print(high_power_fireball("Dragon", 25))

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning])
    for result in sequence("Phoenix", 12):
        print(result)


if __name__ == "__main__":
    main()
