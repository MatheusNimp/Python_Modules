"""Lambda Sanctum exercises.

This module demonstrates lambda expressions with the functional helpers
requested by the subject.
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Return artifacts sorted by power from strongest to weakest."""
    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return mages whose power is greater than or equal to min_power."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name in magical markers."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return max, min, and average power statistics for mages."""
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    powers = list(map(lambda mage: mage["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    """Demonstrate all lambda-based helpers."""
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Moon Amulet", "power": 73, "type": "charm"},
    ]
    mages = [
        {"name": "Alex", "power": 95, "element": "fire"},
        {"name": "Jordan", "power": 70, "element": "water"},
        {"name": "Riley", "power": 40, "element": "earth"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print("Testing power filter...")
    strong_mages = power_filter(mages, 70)
    print(f"Strong mages: {len(strong_mages)}")

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max: {stats['max_power']}, Min: {stats['min_power']}, "
        f"Average: {stats['avg_power']}"
    )


if __name__ == "__main__":
    main()
