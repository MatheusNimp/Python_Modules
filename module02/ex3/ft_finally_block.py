def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("testing normal watering...")
    plants = [
        "tomato",
        "lettuce",
        "carrots"
            ]
    water_plants(plants)
    print("\ntesting with error...")
    plants = [
        "tomato",
        None
            ]
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


def main() -> None:
    test_watering_system()


if __name__ == "__main__":
    main()
