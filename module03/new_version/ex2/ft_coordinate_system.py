import math


PROMPT: str = "Enter new coordinates as floats in format 'x,y,z': "


def get_player_pos() -> tuple[float, float, float]:
    """Prompt until a valid 3D coordinate tuple is provided."""
    while True:
        raw_value: str = input(PROMPT)
        parts: list[str] = raw_value.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError as error:
            invalid_value: str = ""
            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    invalid_value = part.strip()
                    break
            print(f"Error on parameter '{invalid_value}': {error}")


def distance(point_a: tuple[float, float, float],
             point_b: tuple[float, float, float]) -> float:
    """Compute Euclidean distance between two 3D points."""
    return math.sqrt(
        (point_b[0] - point_a[0]) ** 2
        + (point_b[1] - point_a[1]) ** 2
        + (point_b[2] - point_a[2]) ** 2
    )


def main() -> None:
    """Run the coordinate tracking workflow."""
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_pos: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(
        f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}"
    )
    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(distance(first_pos, center), 4):.4f}")

    print("\nGet a second set of coordinates")
    second_pos: tuple[float, float, float] = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance(first_pos, second_pos), 4):.4f}"
    )


if __name__ == "__main__":
    main()
