class Plant:
    """
    Represents a plant with a name, height, and age.
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a Plant object with basic attributes.
        """
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        """
        Displays the plant information in a formatted string.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
    """
    Creates a list of plants and displays their information.
    """
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
            ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.display()


def main():
    """
    Main function that runs the garden data display.
    """
    ft_garden_data()


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    main()
