class Plant:
    """
    Represents a plant with attributes for name, height, and age,
    and methods to simulate growth over time.
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a Plant object with a name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """
        Prints the current information of the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        """
        Increases the plant's height by one unit.
        """
        self.height += 1

    def aging(self):
        """
        Increases the plant's age by one day.
        """
        self.age += 1


def ft_plant_growth():
    """
    Simulates the growth of a plant over one week
    and displays its daily progress.
    """
    plant = Plant("Rose", 25, 30)
    initial_height = plant.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.get_info()
        plant.grow()
        plant.aging()
        print()
    growth = (plant.height - initial_height) - 1
    print(f"Growth this week: +{growth}")


def main():
    """
    Main function that runs the plant growth simulation.
    """
    ft_plant_growth()


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    main()
