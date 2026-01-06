def players_achievements():

    alice = {
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon'
        }

    bob = {
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector'
        }

    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
        }

    def achievements_tracker():
        print("=== Achievement Tracker System ===")

        print(f"\nPlayer alice achievements: {alice}")
        print(f"Player bob achievements: {bob}")
        print(f"Player charlie achievements: {charlie}")

    def achievements_analytics():
        print("\n=== Achievement Analytics ===")

        all_achievements = alice.union(bob).union(charlie)
        print(f"All unique achievements: {all_achievements}")
        print(f"Total unique achievements: {len(all_achievements)}")

        common_to_all = alice.intersection(bob).intersection(charlie)
        print(f"\nCommon to all players: {common_to_all}")

        rare_achievement = all_achievements.difference(alice.intersection(bob).union(
            alice.intersection(charlie).union(bob.intersection(charlie))))
        print(f"Rare achievements (1 player): {rare_achievement}")

        a_vs_b = alice.intersection(bob)
        print(f"\nAlice vs Bob common: {a_vs_b}")
        a = alice.difference(bob)
        print(f"Alice unique: {a}")
        b = bob.difference(alice)
        print(f"Bob unique: {b}", end="")

    achievements_tracker()
    achievements_analytics()


def main():
    players_achievements()


if __name__ == "__main__":
    main()
