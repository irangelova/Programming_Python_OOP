from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    AVAILABLE_CAPACITY = 3

    def __init__(self, name: str):
        super().__init__(name, self.AVAILABLE_CAPACITY)

    def update_salaries(self, min_value: float) -> None:
        engineer_astronauts = [a for a in self.astronauts if a.__class__.__name__ == "EngineerAstronaut"]
        engineer_astronauts_to_increase = [a for a in engineer_astronauts if a.salary <= min_value]
        for astronaut in engineer_astronauts_to_increase:
            astronaut.salary += 3000.0
