#!/usr/bin/env python3

class Plant:
    """A blueprint for creating plant objects that can grow and age."""

    def __init__(self, name: str, height: float, age_plant: int) -> None:
        """Initialize a new plant with the given attributes."""
        self.name = name
        self.height = height
        self.age_plant = age_plant

    def get_info(self) -> str:
        """Return a formatted string containing the plant's current info."""
        return f"{self.name}: {self.height}cm, {self.age_plant} days old"

    def grow(self) -> None:
        """Simulate daily growth by increasing height by 1cm."""
        self.height += 1

    def age(self) -> None:
        """Increase the age of the plant by one day."""
        self.age_plant += 1


def main() -> None:
    """Main program entry point: simulates a week of growth for two plants."""

    names = ("Rose", "Sunflower")
    heights = (25, 30)
    ages = (30, 90)

    plants = (Plant(names[0], heights[0], ages[0]),
              Plant(names[1], heights[1], ages[1]))

    print("=== Day 1 ===")
    for i in range(2):
        print(plants[i].get_info())

    initial_heights = (plants[0].height, plants[1].height)

    for day in range(2, 8):
        for i in range(2):
            plants[i].grow()
            plants[i].age()

    print("=== Day 7 ===")
    for i in range(2):
        print(plants[i].get_info())
        growth = plants[i].height - initial_heights[i]
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
