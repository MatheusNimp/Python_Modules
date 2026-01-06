class Plant:
    """
    Represents a plant with basic attributes and growth behavior.
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a Plant object with name, height, and age.
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


def ft_plant_factory():
    """
    Creates multiple Plant objects from predefined data
    and displays their creation details.
    """
    n_plants = 0
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
        ]

    plants = [Plant(name, height, age) for name, height, age in plants_data]
    print("=== Plant Factory Output ===")
    for plant in plants:
        n_plants += 1
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print(f"\nTotal plants created: {n_plants}")


def main():
    """
    Main function that runs the plant factory process.
    """
    ft_plant_factory()


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    main()
