from typing import Set


def players_achievements() -> None:
    """
    Defines players achievements and runs tracking and analytics reports.
    """

    alice: Set[str] = {
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon'
        }

    bob: Set[str] = {
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector'
        }

    charlie: Set[str] = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
        }

    def achievements_tracker() -> None:
        """
        Displays each player's achievements.
        """
        print("=== Achievement Tracker System ===")

        print(f"\nPlayer alice achievements: {alice}")
        print(f"Player bob achievements: {bob}")
        print(f"Player charlie achievements: {charlie}")

    def achievements_analytics() -> None:
        """
        Performs analytics on players achievements using set operations.
        """
        print("\n=== Achievement Analytics ===")

        all_achievements = alice.union(bob).union(charlie)
        print(f"All unique achievements: {all_achievements}")
        print(f"Total unique achievements: {len(all_achievements)}")

        common_to_all = alice.intersection(bob).intersection(charlie)
        print(f"\nCommon to all players: {common_to_all}")

        rare_achievement = all_achievements.difference(
            alice.intersection(bob).union(
                alice.intersection(charlie).union(
                    bob.intersection(charlie)
                )
            )
        )
        print(f"Rare achievements (1 player): {rare_achievement}")

        a_vs_b = alice.intersection(bob)
        print(f"\nAlice vs Bob common: {a_vs_b}")
        a = alice.difference(bob)
        print(f"Alice unique: {a}")
        b = bob.difference(alice)
        print(f"Bob unique: {b}", end="")

    achievements_tracker()
    achievements_analytics()


def main() -> None:
    """
    Entry point of the program.
    Runs players_achievements().
    """
    players_achievements()


if __name__ == "__main__":
    main()
