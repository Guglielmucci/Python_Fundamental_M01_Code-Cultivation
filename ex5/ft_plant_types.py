#!/usr/bin/env python3


class Plant:
    """A basic class with characteristics common to all plants."""

    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a plant with name, height and age."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """Simulate the increase in height by 1 cm."""
        self.height += 1

    def age_one_day(self) -> None:
        """Increase the age by one day."""
        self.age += 1

    def get_info(self) -> str:
        """Return a formatted string for display."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """A flower with an additional color attribute and blooming ability."""

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        """Initialize a flower using parent constructor and add color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print a message that the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """Extend the basic info with color."""
        return (
                f"{self.name} "
                f"(Flower): "
                f"{self.height:.0f}cm, "
                f"{self.age} days, "
                f"{self.color} color"
               )


class Tree(Plant):
    """A tree with trunk diameter and shade production."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        """Initialize a tree using parent constructor"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and print the shade area based on trunk diameter."""
        shade = self.trunk_diameter * 1.5
        print(f"{self.name} provides {shade:.0f} square meters of shade")

    def get_info(self) -> str:
        """Extend the basic info with trunk diameter."""
        return (
                f"{self.name} (Tree): "
                f"{self.height:.0f}cm, "
                f"{self.age} days, "
                f"{self.trunk_diameter:.0f}cm diameter"
               )


class Vegetable(Plant):
    """A vegetable with harvest season and nutritional value."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        """Initialize a vegetable using parent constructor"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest(self) -> None:
        """Print a message about the vegetable's nutritional value."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self) -> str:
        """Extend the basic info with harvest season."""
        return (
                f"{self.name} (Vegetable): "
                f"{self.height:.0f}cm, "
                f"{self.age} days, "
                f"{self.harvest_season} harvest"
               )


def main() -> None:
    """Create and display a collection of different plant types."""

    plant_data = (
        ("Flower", "Rose", 25.0, 30, "red"),
        ("Flower", "Tulip", 18.0, 25, "yellow"),
        ("Tree", "Oak", 500.0, 1825, 50.0),
        ("Tree", "Pine", 350.0, 1200, 40.0),
        ("Vegetable", "Tomato", 80.0, 90, "summer", "vitamin C"),
        ("Vegetable", "Carrot", 20.0, 60, "autumn", "beta-carotene")
    )

    count = 0
    for _ in plant_data:
        count += 1

    plants = ()
    for i in range(count):
        data = plant_data[i]
        if data[0] == "Flower":
            plants = plants + (Flower(data[1], data[2], data[3], data[4]),)
        elif data[0] == "Tree":
            plants = plants + (Tree(data[1], data[2], data[3], data[4]),)
        elif data[0] == "Vegetable":
            plants = plants + (
                Vegetable(
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5]
                ),
            )

    print("=== Garden Plant Types ===")
    print()
    for i in range(count):
        plant = plants[i]
        plant_type = plant_data[i][0]
        print(plant.get_info())
        if plant_type == "Flower":
            plant.bloom()
        elif plant_type == "Tree":
            plant.produce_shade()
        elif plant_type == "Vegetable":
            plant.harvest()
        print()


if __name__ == "__main__":
    main()
