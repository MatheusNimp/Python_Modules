from ex0.abstractions import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_creature(label: str, creature: Creature) -> None:
    print(f"{label}:")
    print(creature.describe())
    print(creature.attack())

    if isinstance(creature, HealCapability):
        print(creature.heal())


def test_transforming_creature(label: str, creature: Creature) -> None:
    print(f"{label}:")
    print(creature.describe())
    print(creature.attack())

    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    test_healing_creature("base", healing_factory.create_base())
    test_healing_creature("evolved", healing_factory.create_evolved())

    print("\nTesting Creature with transform capability")
    test_transforming_creature("base", transform_factory.create_base())
    test_transforming_creature("evolved", transform_factory.create_evolved())


if __name__ == "__main__":
    main()
