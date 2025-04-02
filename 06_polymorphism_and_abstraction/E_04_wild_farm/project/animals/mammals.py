from typing import List, Type

from project.animals.animal import Mammal
from project.food import Food, Meat, Vegetable, Fruit


class Mouse(Mammal):

    @property
    def allowed_food_types(self) -> List[Type[Food]]:
        return [Vegetable, Fruit]

    @property
    def weight_gain(self) -> float:
        return 0.1

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):

    @property
    def allowed_food_types(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 0.4

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):

    @property
    def allowed_food_types(self) -> List[Type[Food]]:
        return [Meat, Vegetable]

    @property
    def weight_gain(self) -> float:
        return 0.3

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):

    @property
    def allowed_food_types(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gain(self) -> float:
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"
