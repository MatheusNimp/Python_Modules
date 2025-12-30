class Plant:
    def __init__(self, name:	str, height:	int, age:	int):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height):
        if new_height < 0:
            print(
                f"Invalid operation attempted: height {new_height}cm "
                f"[REJECTED]\nSecurity: Negative height rejected\n"
                )
        else:
            self.__height = new_height

    def set_age(self, new_age):
        if new_age < 0:
            print(
                f"Invalid operation attempted: age {new_age}days [REJECTED]"
                f"\nSecurity: Negative age rejected\n"
                )
        else:
            self.__age = new_age

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def grow(self):
        self.set_height(self.__height + 1)
        print(f"{self.name} grew 1cm")

    def aging(self):
        self.set_age(self.__age + 1)

    def get_info(self):
        print(f"- {self.name}: {self.get_height()}cm,"
              f" {self.get_age()} days", end="")

    def plant_type(self):
        return "regular"

    def get_score(self):
        return self.get_height()


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = True

    def get_info(self):
        super().get_info()
        print(f", {self.color} flowers (blooming)", end="")

    def plant_type(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, points):
        super().__init__(name, height, age, color)
        self.points = points

    def get_info(self):
        super().get_info()
        print(f", Prize points: {self.points}")

    def plant_type(self):
        return "prize"

    def get_score(self):
        return self.get_height() + self.points


class GardenManager:
    gardens = []
    garden_count = 0

    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0

        def register_plant(self, plant):
            if plant.plant_type() == "regular":
                self.regular += 1
            elif plant.plant_type() == "flowering":
                self.flowering += 1
            else:
                self.prize += 1

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens = GardenManager.gardens + [self]
        GardenManager.garden_count += 1

    def add_plant(self, plant):
        self.plants = self.plants + [plant]
        self.stats.plants_added += 1
        self.stats.register_plant(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        grown = GardenManager.grow_and_count(self.plants)
        self.stats.total_growth += grown

    def garden_report(self):
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
        count = 0
        for plant in plants:
            plant.grow()
            count += 1
        return count

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.garden_count}")

    @classmethod
    def garden_scores(cls):
        scores = {}
        for garden in cls.gardens:
            total = 0
            for plant in garden.plants:
                total += plant.get_score()
            scores[garden.owner] = total
        return scores


def main():
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
    main()
