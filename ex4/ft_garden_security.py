#!/usr/bin/env python3


class SecurePlant:
    """Protects plant data from invalid modifications."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a plant with name, height and age.
        If values are negative, they are set to 0.
        """
        self.__name = name
        self.__height = 0
        self.__age = 0
        if height >= 0:
            self.__height = height
        if age >= 0:
            self.__age = age

    def get_name(self) -> str:
        """Return the plant's name."""
        return self.__name

    def get_height(self) -> int:
        """Return the current height."""
        return self.__height

    def get_age(self) -> int:
        """Return the current age."""
        return self.__age

    def set_height(self, height: int) -> None:
        """Set a new height, only if non-negative."""
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """Set a new age, only if non-negative."""
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")

    def get_info(self) -> str:
        """Return a string with current data."""
        return f"{self.__name} ({self.__height}cm, {self.__age} days)"


def main() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 20, 25)
    print(f"Plant created: {plant.get_name()}")

    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print()
    print(f"Current plant: {plant.get_info()}")


if __name__ == "__main__":
    main()
