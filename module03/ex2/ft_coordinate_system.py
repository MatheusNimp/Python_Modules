import sys
import math


def parser(coordinates: str):
    try:
        parts = coordinates.split(",")
        if len(parts) != 3:
            raise ValueError("Expected exactly 3 coordinates")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
    return (x, y, z)


def calculate_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    result = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return (result)


def main():
    print("=== Game Coordinate System ===")

    spawn = (0, 0, 0)
    pos1 = (10, 20, 5)
    print(f"Position Created: {pos1}")

    distance1 = calculate_distance(spawn, pos1)
    print(f"Distance betwewn {spawn} and {pos1}: {distance1}")
    if len(sys.argv[1:]) == 1:
        coordinates = sys.argv[1]
        print(f'Parsing coordinates: "{coordinates}"')

    try:
        pos2 = parser(coordinates)
        print(f"Parsed position: {pos2}")

        distance2 = calculate_distance(spawn, pos2)
        print(f"Distance betwewn {spawn} and {pos2}: {distance2}")

        print("\n Unpacking Demonstration:")
        x, y, z = pos2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
