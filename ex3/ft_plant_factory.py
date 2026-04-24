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
    """Main entry point
    creates and displays the plant registry.
    """
    names = ("Rose", "Oak", "Cactus", "Sunflower", "Fern")
    heights = (25, 200, 5, 80, 15)
    ages = (30, 365, 90, 45, 120)

    print("=== Garden Plant Registry ===")

    plant_count = 0
    for i in range(5):
        plant = Plant(names[i], heights[i], ages[i])
        print(plant.get_info())
        plant_count += 1
    print()
    print(f"Total plants created: {plant_count}")


if __name__ == "__main__":
    main()
