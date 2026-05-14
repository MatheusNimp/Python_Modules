from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def get_factory_display_name(factory: object) -> str:
    """Return the display name used in the tournament header."""
    if isinstance(factory, HealingCreatureFactory):
        return "Healing"
    if isinstance(factory, TransformCreatureFactory):
        return "Transform"
    return factory.create_base().name


def get_strategy_display_name(strategy: BattleStrategy) -> str:
    """Return the display name used in the tournament header."""
    return strategy.__class__.__name__.replace("Strategy", "")


def print_tournament_opponents(
    opponents: list[tuple[object, BattleStrategy]]
) -> None:
    """Print tournament opponents using the expected display format."""
    descriptions: list[str] = []

    for factory, strategy in opponents:
        factory_name = get_factory_display_name(factory)
        strategy_name = get_strategy_display_name(strategy)
        descriptions.append(f"({factory_name}+{strategy_name})")

    print(f"[ {', '.join(descriptions)} ]")


def print_strategy_actions(actions: str | list[str]) -> None:
    """Print one or multiple strategy action messages."""
    if isinstance(actions, str):
        print(actions)
        return

    for action in actions:
        print(action)


def battle(opponents: list[tuple[object, BattleStrategy]]) -> None:
    """Make each tournament opponent fight
    once against every other opponent."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]

    for first_index in range(len(creatures)):
        for second_index in range(first_index + 1, len(creatures)):
            first_creature, first_strategy = creatures[first_index]
            second_creature, second_strategy = creatures[second_index]

            print("\n* Battle *")
            print(first_creature.describe())
            print("vs.")
            print(second_creature.describe())
            print("now fight!")

            try:
                print_strategy_actions(first_strategy.act(first_creature))
                print_strategy_actions(second_strategy.act(second_creature))
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    """Run all tournament scenarios."""
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    tournament_0 = [
        (FlameFactory(), normal_strategy),
        (HealingCreatureFactory(), defensive_strategy),
    ]

    tournament_1 = [
        (FlameFactory(), aggressive_strategy),
        (HealingCreatureFactory(), defensive_strategy),
    ]

    tournament_2 = [
        (AquaFactory(), normal_strategy),
        (HealingCreatureFactory(), defensive_strategy),
        (TransformCreatureFactory(), aggressive_strategy),
    ]

    print("Tournament 0 (basic)")
    print_tournament_opponents(tournament_0)
    battle(tournament_0)
    print("\nTournament 1 (error)")
    print_tournament_opponents(tournament_1)
    battle(tournament_1)
    print("\nTournament 2 (multiple)")
    print_tournament_opponents(tournament_2)
    battle(tournament_2)


if __name__ == "__main__":
    main()
