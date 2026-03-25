import sys
import math
from typing import Tuple


def parser(coordinates: str) -> Tuple[int, int, int]:
    """
    Parse a string containing three comma-separated integers
    into a tuple of (x, y, z) coordinates.
    """
    parts = coordinates.split(",")
    if len(parts) != 3:
        raise ValueError("Expected exactly 3 coordinates")

    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def calculate_distance(
    pos1: Tuple[int, int, int],
    pos2: Tuple[int, int, int]
) -> float:
    """
    Calculate the Euclidean distance between two 3D coordinates.
    """
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return (result)


def main() -> None:
    """
    Entry point of the program.
    Demonstrates coordinate parsing, distance calculation,
    and tuple unpacking.
    """
    print("=== Game Coordinate System ===\n")

    spawn = (0, 0, 0)
    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")
    distance1 = calculate_distance(spawn, pos1)
    print(f"Distance between {spawn} and {pos1}: {distance1:.2f}\n")

    if len(sys.argv[1:]) == 1:
        coordinates = sys.argv[1]
        print(f'Parsing coordinates: "{coordinates}"')
        try:
            pos2 = parser(coordinates)
            print(f"Parsed position: {pos2}")
            distance2 = calculate_distance(spawn, pos2)
            print(f"Distance between {spawn} and {pos2}: {distance2:.2f}")

            print("\n Unpacking Demonstration:")
            x, y, z = pos2
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}\n")

        except ValueError as error:
            print(f"Error parsing coordinates: {error}")
            print(f"Error details- Type: ValueError, Args: {error.args}")

    print('Parsing coordinates: "3,4,0"')
    pos_out = parser("3,4,0")
    print(f"Parsed position: {pos_out}")
    print(
        f"Distance between {spawn} and {pos_out}:"
        f" {calculate_distance(spawn, pos_out)}"
        )

    print('\nParsing invalid coordinates: "abc,def,ghi"')
    try:
        parser("abc,def,ghi")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            f"Error details- Type: ValueError,"
            f" Args: {error.args}"
            )

    print("\nUnpacking demonstration:")
    x, y, z = pos_out
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}", end="")


if __name__ == "__main__":
    main()
