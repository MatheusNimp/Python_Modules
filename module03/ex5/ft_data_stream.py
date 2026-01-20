from typing import Generator, Iterator, Tuple


def prng(seed: int) -> Iterator[int]:
    """Return an infinite stream of pseudo-random
     integers using a simple LCG."""
    a = 1103515245
    c = 12345
    m = 2 ** 31
    while True:
        seed = (a * seed + c) % m
        yield seed


def game_event_stream(
    n: int,
    seed: int
) -> Generator[Tuple[str, int, str, str], None, None]:
    """
    Generate n game events using a pseudo-random
     number generator (no random module).
    Yields:
        (player, level, event_type, message)
    """
    rng = prng(seed)

    for i in range(1, n + 1):
        r1 = next(rng)
        r2 = next(rng)
        r3 = next(rng)

        player_selector = r1 % 3
        if player_selector == 0:
            player = "alice"
        elif player_selector == 1:
            player = "bob"
        else:
            player = "charlie"

        level = (r2 % 20) + 1

        event_selector = r3 % 100
        if event_selector < 10:
            event_type = "treasure"
            action = "found treasure"
        elif event_selector < 30:
            event_type = "level_up"
            action = "leveled up"
        else:
            event_type = "kill"
            action = "killed monster"

        message = f"Event {i}: Player {player} (level {level}) {action}"
        yield (player, level, event_type, message)


def fibonacci() -> Iterator[int]:
    """Infinite Fibonacci sequence generator."""
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """Check if a number is prime (simple method for small values)."""
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def primes() -> Iterator[int]:
    """Infinite prime number generator."""
    x = 2
    while True:
        if is_prime(x):
            yield x
        x = x + 1


def main() -> None:
    """
    Entry point of the program.
    Processes a stream of game events and demonstrates generators.
    """
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    seed = 42

    print(f"\nProcessing {total_events} game events...")

    processed = 0
    high_level_players = 0
    treasure_events = 0
    levelup_events = 0

    for player, level, event_type, message in game_event_stream(
                                              total_events, seed):
        processed = processed + 1

        if processed <= 3:
            print(message)
        elif processed == 4:
            print("...")

        if level >= 10:
            high_level_players = high_level_players + 1
        if event_type == "treasure":
            treasure_events = treasure_events + 1
        if event_type == "level_up":
            levelup_events = levelup_events + 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: (not measured)")

    print("\n=== Generator Demonstration ===")

    fib = iter(fibonacci())
    fib_str = ""
    for i in range(10):
        fib_str = fib_str + str(next(fib))
        if i != 9:
            fib_str = fib_str + ", "
    print(f"Fibonacci sequence (first 10): {fib_str}")

    prime_gen = iter(primes())
    prime_str = ""
    for i in range(5):
        prime_str = prime_str + str(next(prime_gen))
        if i != 4:
            prime_str = prime_str + ", "
    print(f"Prime numbers (first 5): {prime_str}", end="")


if __name__ == "__main__":
    main()
