#!/usr/bin/env python3


from typing import Tuple, Optional


class Plant:
    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def info(self) -> str:
        return f"{self.name}: {self.height:.0f}cm"

    def score_value(self) -> float:
        return self.height

    def type_name(self) -> str:
        return "regular"


class FloweringPlant(Plant):
    """A plant that can bloom, distinguished by its color."""

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def info(self) -> str:
        return (
            f"{self.name}: {self.height:.0f}cm, {self.color} flowers "
            "(blooming)"
        )

    def score_value(self) -> float:
        return self.height + 30

    def type_name(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    """A show_winning flower with additional prize points."""

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        prize_points: int
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def info(self) -> str:
        return (
            f"{self.name}: {self.height:.0f}cm, {self.color} flowers "
            f"(blooming), Prize points: {self.prize_points}"
        )

    def score_value(self) -> float:
        return self.height + self.prize_points

    def type_name(self) -> str:
        return "prize"


class Garden:
    """Represents a single garden owned by a person."""

    REGULAR = "regular"
    FLOWERING = "flowering"
    PRIZE = "prize"

    def __init__(self, owner: str) -> None:
        """
        Initialize an empty garden with a given owner.
        """
        self.owner = owner
        self._plants_tuple: Tuple[Plant, ...] = ()
        self._total_growth: float = 0.0
        self._type_counts_tuple: Tuple[int, int, int] = (0, 0, 0)

    def add_plant(self, plant: Plant, verbose: bool = True) -> None:
        """Add a plant to the garden and update counters."""
        self._plants_tuple = self._plants_tuple + (plant,)

        type_name = plant.type_name()

        regular_count, flowering_count, prize_count = self._type_counts_tuple

        if type_name == Garden.REGULAR:
            self._type_counts_tuple = (
                regular_count + 1,
                flowering_count,
                prize_count
            )
        elif type_name == Garden.FLOWERING:
            self._type_counts_tuple = (
                regular_count,
                flowering_count + 1,
                prize_count
            )
        elif type_name == Garden.PRIZE:
            self._type_counts_tuple = (
                regular_count,
                flowering_count,
                prize_count + 1
            )

        if verbose:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def get_plant_count(self) -> int:
        """Restituisce il numero di piante (lunghezza della tupla)."""
        count = 0
        for _ in self._plants_tuple:
            count += 1
        return count

    def get_plants(self) -> Tuple[Plant, ...]:
        """Restituisce la tupla delle piante (sola lettura)."""
        return self._plants_tuple

    def get_type_counts(self) -> Tuple[str, int, str, int, str, int]:
        """Restituisce i conteggi come una tupla piatta di coppie."""
        regular, flowering, prize = self._type_counts_tuple
        return ("regular", regular, "flowering", flowering, "prize", prize)

    def get_type_count(self, type_name: str) -> int:
        """Ottiene il conteggio per un tipo specifico."""
        regular, flowering, prize = self._type_counts_tuple

        if type_name == Garden.REGULAR:
            return regular
        elif type_name == Garden.FLOWERING:
            return flowering
        elif type_name == Garden.PRIZE:
            return prize
        return 0

    def help_grow(self) -> None:
        """Simulate one day of growth for all plants in the garden."""
        print(f"{self.owner} is helping all plants grow...")

        plant_count = 0
        for _ in self._plants_tuple:
            plant_count += 1

        for i in range(plant_count):
            plant = self._plants_tuple[i]
            plant.grow()
            self._total_growth += 1.0
            print(f"{plant.name} grew 1cm")
        print()


class GardenManager:
    """Manages multiple gardens and provides analytics."""

    class GardenStats:
        """Nested helper class for calculating garden statistics."""

        @staticmethod
        def total_plants(garden: Garden) -> int:
            return garden.get_plant_count()

        @staticmethod
        def total_growth(garden: Garden) -> float:
            return garden._total_growth

        TypeCounts = Tuple[str, int, str, int, str, int]

        @staticmethod
        def plant_type_counts(garden: Garden) -> TypeCounts:
            """Return type counts as a flat tuple."""
            return garden.get_type_counts()

    def __init__(self) -> None:
        """Initialize an empty manager with no gardens."""
        self._gardens_tuple: Tuple[Tuple[str, Garden], ...] = ()

    def add_garden(self, garden: Garden) -> None:
        """Add a garden to the manager."""
        self._gardens_tuple = self._gardens_tuple + ((garden.owner, garden),)

    def get_garden(self, owner: str) -> Optional[Garden]:
        """Retrieve a garden by owner's name."""
        garden_count = 0
        for _ in self._gardens_tuple:
            garden_count += 1

        for i in range(garden_count):
            garden_owner, garden = self._gardens_tuple[i]
            if garden_owner == owner:
                return garden
        return None

    def get_garden_count(self) -> int:
        """Restituisce il numero di giardini."""
        count = 0
        for _ in self._gardens_tuple:
            count += 1
        return count

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        """
        Factory method that creates a manager with two prepopulated gardens.
        """
        manager = cls()

        alice = Garden("Alice")
        alice.add_plant(Plant("Oak Tree", 100.0, 30))
        alice.add_plant(FloweringPlant("Rose", 25.0, 30, "red"))
        alice.add_plant(PrizeFlower("Sunflower", 50.0, 45, "yellow", 10))
        manager.add_garden(alice)
        print()

        bob = Garden("Bob")
        bob.add_plant(Plant("Spruce", 50.0, 10), verbose=False)
        bob.add_plant(
            FloweringPlant("Violet", 12.0, 20, "purple"),
            verbose=False
        )
        manager.add_garden(bob)

        return manager

    @staticmethod
    def validate_heights(garden: Garden) -> bool:
        """Check that all plants in the garden have non_negative height."""
        plants = garden.get_plants()

        plant_count = 0
        for _ in plants:
            plant_count += 1
        for i in range(plant_count):
            if plants[i].height < 0:
                return False
        return True

    @staticmethod
    def calculate_score(garden: Garden) -> float:
        """
        Calculate the total score of a garden using polymorphic score_value().
        """
        total = 0.0
        plants = garden.get_plants()

        plant_count = 0
        for _ in plants:
            plant_count += 1

        for i in range(plant_count):
            total += plants[i].score_value()
        return total

    def garden_report(self, owner: str) -> None:
        """Print a detailed report for the garden owned by 'owner'."""
        garden = self.get_garden(owner)
        if not garden:
            print(f"Garden '{owner}' not found.")
            return

        stats = self.GardenStats
        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")

        plants = garden.get_plants()
        plant_count = 0
        for _ in plants:
            plant_count += 1
        for i in range(plant_count):
            print(f"- {plants[i].info()}")
        print()
        print(
            f"Plants added: {stats.total_plants(garden)}, "
            f"Total growth: {stats.total_growth(garden):.0f}cm"
        )
        counts_tuple = stats.plant_type_counts(garden)
        print(
            f"Plant types: {counts_tuple[1]} regular, "
            f"{counts_tuple[3]} flowering, {counts_tuple[5]} prize flowers"
        )
        print()


def main() -> None:
    """Demonstrate the garden management system."""
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network()

    alice = manager.get_garden("Alice")
    alice.help_grow()

    manager.garden_report("Alice")

    print(f"Height validation test: {manager.validate_heights(alice)}")

    alice_score = manager.calculate_score(alice)
    bob = manager.get_garden("Bob")
    bob_score = manager.calculate_score(bob)
    print(f"Garden scores - Alice: {alice_score:.0f}, Bob: {bob_score:.0f}")

    print(f"Total gardens managed: {manager.get_garden_count()}")


if __name__ == "__main__":
    main()
