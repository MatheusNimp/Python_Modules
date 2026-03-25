import random
import typing


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Yield endless random player events."""
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    """Yield and remove random events until the list is empty."""
    while len(events) > 0:
        index: int = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    """Generate and consume game events."""
    print("=== Game Data Stream Processor ===")
    event_generator: typing.Generator[
        tuple[str, str], None, None] = gen_event()

    for index in range(1000):
        event: tuple[str, str] = next(event_generator)
        print(f"Event {index}: Player {event[0]} did action {event[1]}")

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(event_generator))
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
