class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def main():
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
