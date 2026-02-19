import alchemy.transmutation


def main() -> None:
    print("=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(
        f"philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}"
    )
    print(
        f"elixir_of_life(): "
        f"{alchemy.transmutation.elixir_of_life()}"
    )

    print("\nTesting Package Access:")
    print(
        f"alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}"
    )

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
