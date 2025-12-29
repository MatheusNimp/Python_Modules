class SecurePlant:
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
			print(f"Height updated: {self.__height}cm [OK]")

	def get_height(self):
		return self.__height

	def set_age(self, new_age):
		if new_age < 0:
			print(f"Invalid operation attempted: age {new_age}days [REJECTED]"
		 f"\nSecurity: Negative age rejected\n")
		else:
			self.__age = new_age
			print(f"Age updated: {self.__age} days [OK]")

	def get_age(self):
		return self.__age

	def get_info(self):
		print(f"\nCurrent plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)")

	def grow(self):
		self.set_height(self.__height + 1)

	def aging(self):
		self.set_age(self.__age + 1)

