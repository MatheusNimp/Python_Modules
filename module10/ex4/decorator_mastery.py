import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable) -> Callable:
    """Decorate a function to display execution timing information."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Return a decorator that validates the first power argument."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power_index = 0
            if args and not isinstance(args[0], int):
                power_index = 2 if len(args) > 2 else 1

            power = kwargs.get("power")
            if power is None and len(args) > power_index:
                power = args[power_index]

            if not isinstance(power, int) or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Return a decorator that retries exceptions up to max_attempts."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """Simple guild class demonstrating staticmethod and method decorators."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True when name has at
        least 3 chars and only letters/spaces."""
        return len(name) >= 3 and all(
            character.isalpha() or character.isspace()
            for character in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a guild spell when its power is valid."""
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Demo timed spell."""
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def failing_spell() -> str:
    """Demo spell that always fails."""
    raise RuntimeError("unstable mana")


@retry_spell(3)
def orc_spell() -> str:
    """Demo spell that succeeds immediately."""
    return "Waaaaaaagh spelled !"


def main() -> None:
    """Demonstrate decorators and static methods."""
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("Testing retrying spell...")
    print(failing_spell())
    print(orc_spell())

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("X1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
