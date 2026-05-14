from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print(base_creature.describe())
    print(base_creature.attack())

    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle(factory_one: CreatureFactory, factory_two: CreatureFactory) -> None:
    print("\nTesting battle")

    creature_one = factory_one.create_base()
    creature_two = factory_two.create_base()

    print(creature_one.describe())
    print("vs.")
    print(creature_two.describe())
    print("fight!")
    print(creature_one.attack())
    print(creature_two.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
