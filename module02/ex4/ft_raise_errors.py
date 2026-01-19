def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> str:
    """
    Validate plants health conditions and return it`s health status
    """
    if not plant_name:
        raise ValueError("Plant name cannont be empty!\n")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")

    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)\n"
            )
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)\n"
            )

    return (f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    """
    Tests some cases for valid inputs and exceptions
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("Tomato", 4, 5))
    except ValueError as error:
        print(f"Error: {error}")

    print("Testing empty plant name...")
    try:
        print(check_plant_health(None, 4, 5))
    except ValueError as error:
        print(f"Error: {error}")

    print("Testing bad water level...")
    try:
        print(check_plant_health("Tomato", 15, 5))
    except ValueError as error:
        print(f"Error: {error}")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("Tomato", 4, 0))
    except ValueError as error:
        print(f"Error: {error}")
    print("All error raising testes completed!", end="")


def main():
    """
    Entry point of the program
    Runs test_plant_checks()
    """
    test_plant_checks()


if __name__ == "__main__":
    main()
