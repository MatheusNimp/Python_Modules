class Plant:
    """
    Base class representing a generic plant with common attributes.
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a Plant with name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """
        Prints basic information about the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days", end="")


class Flower(Plant):
    """
    Represents a flower plant with a specific color.
    """
    def __init__(self, name, height, age, color):
        """
        Initializes a Flower with an additional color attribute.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Simulates the flower blooming.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        """
        Prints detailed information about the flower.
        """
        print(f"{self.name} (Flower): ", end="")
        super().get_info()
        print(f", {self.color} color")


class Tree(Plant):
    """
    Represents a tree with a trunk diameter attribute.
    """
    def __init__(self, name, height, age, trunk_diameter):
        """
        Initializes a Tree with trunk diameter information.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculates and displays the shade area produced by the tree.
        """
        shade_area = self.trunk_diameter * 1.5
        print(f"{self.name} provides {shade_area} square meters of shade")

    def get_info(self):
        """
        Prints detailed information about the tree.
        """
        print(f"{self.name} (Tree): ", end="")
        super().get_info()
        print(f", {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable plant with harvest and nutritional details.
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initializes a Vegetable with harvest season and nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        """
        Prints detailed information about the vegetable.
        """
        print(f"{self.name} (Vegetable): ", end="")
        super().get_info()
        print(f", {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}", end="")


def main():
    """
    Main function that demonstrates different plant types.
    """
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    rose.get_info()
    rose.bloom()
    print()
    oak.get_info()
    oak.produce_shade()
    print()
    tomato.get_info()


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    main()
