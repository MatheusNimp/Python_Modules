class Plant:
    def __init__(self, name:	str, height:	int, age:	int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += 1

    def aging(self):
        self.age += 1


def ft_plant_growth():
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
    ft_plant_growth()


if __name__ == "__main__":
    main()
