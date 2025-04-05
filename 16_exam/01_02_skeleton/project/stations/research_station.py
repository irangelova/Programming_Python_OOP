from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    AVAILABLE_CAPACITY = 5

    def __init__(self, name: str):
        super().__init__(name, self.AVAILABLE_CAPACITY)

    def update_salaries(self, min_value: float) -> None:
        scientist_astronauts = [a for a in self.astronauts if a.__class__.__name__ == "ScientistAstronaut"]
        scientist_astronauts_to_increase = [a for a in scientist_astronauts if a.salary <= min_value]
        for astronaut in scientist_astronauts_to_increase:
            astronaut.salary += 5000.0
