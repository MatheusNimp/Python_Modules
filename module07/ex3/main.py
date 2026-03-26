from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("Simulating aggressive turn...")
    print(f"Hand: {engine.hand}")
    turn_result = engine.simulate_turn()
    print("Turn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {turn_result}")
    print("Game Report:")
    print(engine.get_engine_status())
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
