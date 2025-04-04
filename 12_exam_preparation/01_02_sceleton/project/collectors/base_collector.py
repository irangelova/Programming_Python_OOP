from abc import ABC, abstractmethod
from typing import List

from project.artifacts.base_artifact import BaseArtifact
import re

class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: List[BaseArtifact] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not re.match(r'^[a-zA-Z0-9 ]+$', value): #check with for if char not in isalphanum...
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value

    @property
    def available_money(self):
        return self.__available_money

    @available_money.setter
    def available_money(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space

    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int) -> bool:
        return artifact_price <= self.available_money and artifact_space_required <= self.available_space

    def __str__(self):
        artifacts_list = ", ".join(sorted([a.name for a in self.purchased_artifacts], key=lambda x: x, reverse=True)
                                   ) if self.purchased_artifacts else "none"
        return (f"Collector name: {self.name}; Money available: {self.available_money:.2f};"
                f" Space available: {self.available_space}; Artifacts: {artifacts_list}")

