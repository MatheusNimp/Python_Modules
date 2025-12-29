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


def ft_plant_factory():
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
    ft_plant_factory()


if __name__ == "__main__":
    main()
