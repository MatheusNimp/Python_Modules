class Plant:
	def __init__(self, name:	str, height:	int, age:	int):
		self.name = name
		self.__height = 0
		self.__age = 0
		self.set_height(height)
		self.set_age(age)

	def set_height(self, new_height):
		if new_height < 0:
			print(f"Invalid operation attempted: height {new_height}cm [REJECTED]"
		 f"\nSecurity: Negative height rejected\n")
		else:
			self.__height = new_height

	def set_age(self, new_age):
		if new_age < 0:
			print(f"Invalid operation attempted: age {new_age}days [REJECTED]"
		 f"\nSecurity: Negative age rejected\n")
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
		print(f"- {self.name}: {self.get_height()}cm, {self.get_age()} days", end="")


class FloweringPlant(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self.color = color
		self.blooming = True

	def get_info(self):
		super().get_info()
		print(f", {self.color} flowers (blooming)", end="")


class PrizeFlower(FloweringPlant):
	def __init__(self, name, height, age, color, points):
		super().__init__(name, height, age, color)
		self.points = points

	def get_info(self):
		super().get_info()
		print(f", Prize points: {self.points}")


class GardenManager:
	gardens = []

	class GardenStats:
		def __init__(self):
			self.plants = 0
			self.total_growth = 0

	def __init__(self, owner):
		self.owner = owner
		self.plants = []

