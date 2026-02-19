import alchemy
import alchemy.elements


def safe_call(label: str, func) -> None:
    try:
        result: str = func()
        print(f"{label}: {result}")
    except AttributeError as error:
        print(f"{label}: {error}")


def main() -> None:
    print("=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    safe_call("alchemy.create_fire()", alchemy.create_fire)
    safe_call("alchemy.create_water()", alchemy.create_water)

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
