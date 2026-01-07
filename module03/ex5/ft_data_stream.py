def prng(seed):
    """Return an infinite stream of pseudo-random
     integers using a simple LCG."""
    a = 1103515245
    c = 12345
    m = 2 ** 31
    while True:
        seed = (a * seed + c) % m
        yield seed


def game_event_stream(n, seed):
    """
    Generate n game events using a pseudo-random
     number generator (no random module).
    Yields: (player, level, event_type, message)
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
        if event_selector < 10 == 0:
            event_type = "treasure"
            action = "found_treasure"
        elif event_selector < 30:
            event_type = "level_up"
            action = "leveled up"
        else:
            event_type = "kill"
            action = "killed a monster"

        message = f"Event {i}: Player {player} (level {level}) {action}"
        yield (player, level, event_type, message)


def fibonacci():
    """
    Infinite Fibonacci sequence generator.
    """
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def primes():
    """
    Infinite prime number generator.
    """
    x = 2
    while True:
        if is_prime(x):
            yield x
        x = x + 1
