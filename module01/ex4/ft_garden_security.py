"""
Garden Security System
Exercise 4 - ft_garden_security

This module demonstrates data encapsulation and protection
using custom getter and setter methods.
"""


class SecurePlant:
    """
    Represents a plant with protected attributes for height and age.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a SecurePlant with validated initial values.
        """
        self.name = name
        self.__height = 0
        self.__age = 0

        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, new_height: int):
        """
        Sets the plant height if the value is valid.
        """
        if new_height < 0:
            print(
                f"Invalid operation attempted: height"
                f" {new_height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")

    def get_height(self) -> int:
        """
        Returns the current height of the plant.
        """
        return self.__height

    def set_age(self, new_age: int):
        """
        Sets the plant age if the value is valid.
        """
        if new_age < 0:
            print(
                f"Invalid operation attempted: age {new_age} days [REJECTED]"
            )
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")

    def get_age(self) -> int:
        """
        Returns the current age of the plant.
        """
        return self.__age

    def get_info(self):
        """
        Prints the current state of the plant.
        """
        print(
            f"\nCurrent plant: {self.name} "
            f"({self.get_height()}cm, {self.get_age()} days)", end=""
        )

    def grow(self):
        """
        Increases the plant height by one unit using validation.
        """
        self.set_height(self.__height + 1)

    def aging(self):
        """
        Increases the plant age by one day using validation.
        """
        self.set_age(self.__age + 1)


def main():
    """
    Demonstrates the Garden Security System.
    """
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)

    print()

    plant.set_height(-5)

    plant.get_info()


if __name__ == "__main__":
    main()
