import sys


def main() -> None:
    """Process score arguments and print statistics."""
    print("=== Player Score Analytics ===")
    scores: list[float] = []

    for arg in sys.argv[1:]:
        try:
            value: float = float(arg)
            if value.is_integer():
                scores.append(int(value))
            else:
                scores.append(value)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    total_score: float = sum(scores)
    average_score: float = total_score / len(scores)
    high_score: float = max(scores)
    low_score: float = min(scores)
    score_range: float = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
