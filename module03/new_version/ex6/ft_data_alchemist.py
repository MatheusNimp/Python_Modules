import random


PLAYER_NAMES: list[str] = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]
MIN_SCORE: int = 0
MAX_SCORE: int = 1000


def main() -> None:
    """Demonstrate list and dictionary comprehensions."""
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {PLAYER_NAMES}")

    capitalized_names: list[str] = [name.capitalize() for name in PLAYER_NAMES]
    already_capitalized: list[str] = [
        name for name in PLAYER_NAMES if name == name.capitalize()
    ]

    print(f"New list with all names capitalized: {capitalized_names}")
    print(f"New list of capitalized names only: {already_capitalized}")

    score_dict: dict[str, int] = {
        name: random.randint(MIN_SCORE, MAX_SCORE)
        for name in capitalized_names
    }
    print(f"\nScore dict: {score_dict}")

    average_score: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average_score}")

    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items()
        if score > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
