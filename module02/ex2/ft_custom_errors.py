class GardenError(Exception):
    """
    A father class for all garden-related exceptions.
    """
    pass


class PlantError(GardenError):
    """
    Class to handle specific exceptions related to plants.
    """
    pass


class WaterError(GardenError):
    """
    Class to handle specific exceptions related to water.
    """
    pass


def raise_plant_error() -> None:
    """
    Raises an error related to plant issues.
    """
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    """
    Raises an error related to water issues.
    """
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    """
    Entry point of the program.
    Runs methods to verify custom garden errors.
    """
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError:")
    try:
        raise_plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    for func in (raise_plant_error, raise_water_error):
        try:
            func()
        except GardenError as error:
            print(f"Caught a garden error: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
