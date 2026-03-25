import random


ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Speed Runner",
    "Treasure Hunter",
    "Crafting Genius",
    "World Savior",
    "Boss Slayer",
    "Collector Supreme",
    "Master Explorer",
    "Sharp Mind",
    "Survivor",
    "Strategist",
    "Untouchable",
    "Unstoppable",
    "Hidden Path Finder",
]
PLAYERS: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set[str]:
    """Generate a random set of achievements for one player."""
    total: int = random.randint(5, 10)
    return set(random.sample(ACHIEVEMENTS, total))


def main() -> None:
    """Generate and compare player achievements."""
    print("=== Achievement Tracker System ===\n")
    player_sets: dict[str, set[str]] = {}

    for player in PLAYERS:
        player_sets[player] = gen_player_achievements()
        print(f"Player {player}: {player_sets[player]}")

    all_distinct: set[str] = set()
    for achievements in player_sets.values():
        all_distinct = all_distinct.union(achievements)
    print(f"\nAll distinct achievements: {all_distinct}")

    common_achievements: set[str] = player_sets[PLAYERS[0]].copy()
    for player in PLAYERS[1:]:
        common_achievements = common_achievements.intersection(
            player_sets[player])
    print(f"\nCommon achievements: {common_achievements}\n")

    for player in PLAYERS:
        others_union: set[str] = set()
        for other_player in PLAYERS:
            if other_player != player:
                others_union = others_union.union(player_sets[other_player])
        only_this_player: set[str] = player_sets[player].difference(
            others_union)
        print(f"Only {player} has: {only_this_player}")

    print()

    for player in PLAYERS:
        missing: set[str] = set(ACHIEVEMENTS).difference(player_sets[player])
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
