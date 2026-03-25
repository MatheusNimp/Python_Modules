import sys


def main() -> None:
    """
    Entry point of the program.
    Processes command-line arguments as player scores and
    prints basic statistical analysis.
    """
    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    if len(args) == 0:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score_1> <score_2> ..."
              )
        return

    scores = []
    for arg in args:
        try:
            scores = scores + [int(arg)]
        except ValueError:
            print("Error: All scores must be integers")
            return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
