class GardenError(Exception):
    """
    A father Class to all garden exceptions
    """
    pass


class PlantError(GardenError):
    """
    Class to handle specific exceptions related to plants
    """
    pass


class TankError(GardenError):
    """
    Class to handle specific exceptions related to the water tank
    """
    pass


class WaterError(GardenError):
    """
    Class to handle specific exceptions related to water
    """
    pass


class HealthCheckError(GardenError):
    """
    Class to handle specific exceptions related to plants health
    """
    pass


class GardenManager:
    """
    Class to manage the plants and the water tank
    """
    MAX_TANK = 10

    def __init__(self) -> None:
        """
        Initialize the garden with a empety plants list and a standard tank
        """
        self.plants = {}
        self.water_tank = 5

    def add_plant(self, name: str, water: int, sun: int) -> None:
        """
        Add a plant to to the garden
        """
        if not name:
            raise PlantError("Plant name cannot be empty!")

        if name in self.plants:
            raise PlantError(f"The plant '{name}' already exists!")

        self.plants[name] = {
            "water": water,
            "sun": sun
        }
        print(f"Added {name} successfully")

    def fill_tank(self, amount: int) -> None:
        """
        If possible, fill the water tank
        """
        if amount <= 0:
            raise TankError("Fill amount must be positive")

        if self.water_tank + amount > self.MAX_TANK:
            raise TankError("Tank is already full")

        self.water_tank += amount
        print(f"Tank filled. Current water level: {self.water_tank}")

    def water_plants(self) -> None:
        """
        Water the plants
        """
        if self.water_tank <= 0:
            raise WaterError("Not enough water in tank")

        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_tank <= 0:
                    raise WaterError("Not enough water in tank")

                self.plants[plant]["water"] += 1
                self.water_tank -= 1
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str) -> None:
        """
        verify the plants health
        """
        if name not in self.plants:
            raise HealthCheckError(f"Plant {name} not found")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]

        if water < 1:
            raise HealthCheckError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise HealthCheckError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise HealthCheckError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise HealthCheckError(
                f"Sunlight hours {sun} is too high (max 12)"
                                   )

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def main() -> None:
    """
    Entry point of the program
    Runs the previous methods to simulate the garden management system
    """
    print("=== Garden Management System ===\n")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
        manager.add_plant("lettuce", 15, 8)
        manager.add_plant("", 3, 6)
    except PlantError as error:
        print(f"Error adding plant: {error}")

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except WaterError as error:
        print(f"Error watering plants: {error}")

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato")
        manager.check_plant_health("lettuce")
    except HealthCheckError as error:
        print(f"Error checking lettuce: {error}")

    print("\nTesting error recovery...")
    try:
        manager.water_tank = 0
        manager.water_plants()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!", end="")


if __name__ == "__main__":
    main()
