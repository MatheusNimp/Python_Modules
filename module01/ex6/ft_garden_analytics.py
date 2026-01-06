class Plant:
    """
    Represents a plant with protected height and age attributes,
    including validation and basic growth behavior.
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a Plant object and validates the initial height and age.
        """
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height):
        """
        Sets the plant height if the value is valid.
        """
        if new_height < 0:
            print(
                f"Invalid operation attempted: height {new_height}cm "
                f"[REJECTED]\nSecurity: Negative height rejected\n"
                )
        else:
            self.__height = new_height

    def set_age(self, new_age):
        """
        Sets the plant age if the value is valid.
        """
        if new_age < 0:
            print(
                f"Invalid operation attempted: age {new_age}days [REJECTED]"
                f"\nSecurity: Negative age rejected\n"
                )
        else:
            self.__age = new_age

    def get_height(self):
        """
        Returns the current height of the plant.
        """
        return self.__height

    def get_age(self):
        """
        Returns the current age of the plant.
        """
        return self.__age

    def grow(self):
        """
        Increases the plant height by one unit and prints the growth action.
        """
        self.set_height(self.__height + 1)
        print(f"{self.name} grew 1cm")

    def aging(self):
        """
        Increases the plant age by one day.
        """
        self.set_age(self.__age + 1)

    def get_info(self):
        """
        Prints formatted information about the plant.
        """
        print(f"- {self.name}: {self.get_height()}cm,"
              f" {self.get_age()} days", end="")

    def plant_type(self):
        """
        Returns the type label for the plant.
        """
        return "regular"

    def get_score(self):
        """
        Returns the score used for garden scoring.
        """
        return self.get_height()


class FloweringPlant(Plant):
    """
    Represents a flowering plant with a color attribute.
    """
    def __init__(self, name, height, age, color):
        """
        Initializes a FloweringPlant with an additional color attribute.
        """
        super().__init__(name, height, age)
        self.color = color
        self.blooming = True

    def get_info(self):
        """
        Prints formatted information about the flowering plant.
        """
        super().get_info()
        print(f", {self.color} flowers (blooming)", end="")

    def plant_type(self):
        """
        Returns the type label for the plant.
        """
        return "flowering"


class PrizeFlower(FloweringPlant):
    """
    Represents a flowering plant that includes prize points for scoring.
    """
    def __init__(self, name, height, age, color, points):
        """
        Initializes a PrizeFlower with an additional points attribute.
        """
        super().__init__(name, height, age, color)
        self.points = points

    def get_info(self):
        """
        Prints formatted information about the prize flower.
        """
        super().get_info()
        print(f", Prize points: {self.points}")

    def plant_type(self):
        """
        Returns the type label for the plant.
        """
        return "prize"

    def get_score(self):
        """
        Returns the score for the prize flower including bonus points.
        """
        return self.get_height() + self.points


class GardenManager:
    """
    Manages a garden of plants for a given owner and tracks garden statistics.
    """
    gardens = []
    garden_count = 0

    class GardenStats:
        """
        Tracks statistics for a specific garden,
        including plant counts and growth.
        """
        def __init__(self):
            """
            Initializes counters used to track garden statistics.
            """
            self.plants_added = 0
            self.total_growth = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0

        def register_plant(self, plant):
            """
            Updates plant type counters based on the plant type.
            """
            if plant.plant_type() == "regular":
                self.regular += 1
            elif plant.plant_type() == "flowering":
                self.flowering += 1
            else:
                self.prize += 1

    def __init__(self, owner):
        """
        Initializes a GardenManager for an
        owner and registers it in the network.
        """
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens = GardenManager.gardens + [self]
        GardenManager.garden_count += 1

    def add_plant(self, plant):
        """
        Adds a plant to the garden and updates tracking statistics.
        """
        self.plants = self.plants + [plant]
        self.stats.plants_added += 1
        self.stats.register_plant(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        """
        Grows all plants in the garden and updates total growth statistics.
        """
        print(f"{self.owner} is helping all plants grow...")
        grown = GardenManager.grow_and_count(self.plants)
        self.stats.total_growth += grown

    def garden_report(self):
        """
        Prints a report of the garden plants and summary statistics.
        """
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()
            print()
        print(
            f"Plants added: {self.stats.plants_added}, "
            f"Total growth: {self.stats.total_growth}cm"
            )
        print(
            f"Plant types: {self.stats.regular} regular, "
            f"{self.stats.flowering} flowering, "
            f"{self.stats.prize} prize flowers"
            )
        print()

    @staticmethod
    def grow_and_count(plants):
        """
        Grows each plant in a list and returns how many were processed.
        """
        count = 0
        for plant in plants:
            plant.grow()
            count += 1
        return count

    @classmethod
    def create_garden_network(cls):
        """
        Prints how many gardens are currently managed in the network.
        """
        print(f"Total gardens managed: {cls.garden_count}", end="")

    @classmethod
    def garden_scores(cls):
        """
        Calculates and returns a score for each garden based on its plants.
        """
        scores = {}
        for garden in cls.gardens:
            total = 0
            for plant in garden.plants:
                total += plant.get_score()
            scores[garden.owner] = total
        return scores


def main():
    """
    Main function that demonstrates the garden management system.
    """
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    matheus = GardenManager("Matheus")

    oak = Plant("Oak Tree", 100, 500)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 90, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print()

    cactus = Plant("Cactus", 40, 200)
    tulip = FloweringPlant("Tulip", 20, 15, "purple")
    orchid = PrizeFlower("Orchid", 35, 60, "white", 25)

    matheus.add_plant(cactus)
    matheus.add_plant(tulip)
    matheus.add_plant(orchid)
    print()

    alice.help_plants_grow()
    print()
    matheus.help_plants_grow()
    print()

    alice.garden_report()
    matheus.garden_report()

    scores = GardenManager.garden_scores()
    print(
        f"Garden scores - Alice: {scores['Alice']}, "
        f"Matheus: {scores['Matheus']}"
    )

    GardenManager.create_garden_network()


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    main()
