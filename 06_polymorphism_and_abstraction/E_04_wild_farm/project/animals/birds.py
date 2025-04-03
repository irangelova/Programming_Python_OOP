from typing import List, Type

from project import Bird
from project import Meat, Food, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def allowed_food_types(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def allowed_food_types(self) -> List[Type[Food]]:
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def weight_gain(self) -> float:
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
