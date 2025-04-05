from abc import ABC, abstractmethod
import re
from typing import List

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: List[BaseAstronaut] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not re.match(r'^[a-zA-Z0-9-]+$', value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self) -> str:
        total_salary = sum([a.salary for a in self.astronauts])
        return f"{total_salary:.2f}"

    def status(self) -> str:
        astronauts_sorted = sorted([a.id_number for a in self.astronauts], key=lambda x: x) if self.astronauts else "N/A"

        result = [f"Station name: {self.name}"]
        if "N/A" in astronauts_sorted:
            result.append(f"Astronauts: N/A")
        else:
            astronauts = []
            for astronaut in astronauts_sorted:
                astronauts.append(astronaut)
            result.append(f"Astronauts: {' #'.join(astronauts)}")
        result.append(f"Total salaries: {self.calculate_total_salaries()}")

        return "; ".join(result)

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass
