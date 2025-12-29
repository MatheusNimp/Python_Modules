class Plant:
	def __init__(self, name:	str, height:	int, age:	int):
		self.name = name
		self.height = height
		self.age = age

	def get_info(self):
		print(f": {self.height}cm, {self.age} days")


class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color

	def bloom(self):
		print(f"{self.name} is blooming beautifully!")

	def get_info(self):
		print(f"{self.name} (Flower)")
		super().get_info()
		print(f", {self.color} color")


class Tree(Plant):
	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self):
		shade_area = self.trunk_diameter * 1.5
		print(f"{self.name} provides {shade_area} square meters of shade")

	def get_info(self):
		print(f"{self.name} (Tree)")
		super().get_info()
		print(f", {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
	def __init__(self, name, height, age, harvest_season, nutritional_value):
		super().__init__(name, height, age)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value

	def get_info(self):
		print(f"{self.name} (Vegetable)")
		super().get_info()
		print(f", {self.harvest_season}\n{self.name}"
		f" is rich in {self.nutritional_value}")
