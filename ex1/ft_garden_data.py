#!/usr/bin/env python3


class Plant:
    """A blueprint for creating plant objects."""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a new plant with the given attributes."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return a formatted string containing the plant's information."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """Main entry point: creates and displays the plant registry."""
    names = ("Rose", "Sunflower", "Cactus")
    heights = (25, 80, 15)
    ages = (30, 45, 120)

    print("=== Garden Plant Registry ===")

    for i in range(3):
        plant = Plant(names[i], heights[i], ages[i])
        print(plant.get_info())


if __name__ == "__main__":
    main()
