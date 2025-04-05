from typing import List, Type

from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    VALID_ASTRONAUTS: List[Type[BaseAstronaut]] = [EngineerAstronaut, ScientistAstronaut]
    VALID_STATIONS: List[Type[BaseStation]] = [ResearchStation, MaintenanceStation]

    def __init__(self):
        self.astronauts: List[BaseAstronaut] = []
        self.stations: List[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float) -> str:
        astronaut_class = next((a for a in self.VALID_ASTRONAUTS if a.__name__ == astronaut_type), None)
        if astronaut_class is None:
            raise ValueError("Invalid astronaut type!")

        if any(a.id_number == astronaut_id_number for a in self.astronauts):
            raise ValueError(f"{astronaut_id_number} has been already added!")

        astronaut = astronaut_class(astronaut_id_number, astronaut_salary)
        self.astronauts.append(astronaut)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str) -> str:
        station_class = next((s for s in self.VALID_STATIONS if s.__name__ == station_type), None)
        if station_class is None:
            raise ValueError("Invalid station type!")

        if any(s.name == station_name for s in self.stations):
            raise ValueError(f"{station_name} has been already added!")

        station = station_class(station_name)
        self.stations.append(station)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str) -> str:
        station = next((s for s in self.stations if s.name == station_name), None)
        if station is None:
            raise ValueError(f"Station {station_name} does not exist!")

        astronaut = next((a for a in self.astronauts if a.__class__.__name__ == astronaut_type), None)
        if astronaut is None:
            raise ValueError("No available astronauts of the type!")

        if station.capacity == 0:
            return f"This station has no available capacity."

        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1
        return f"{astronaut.id_number} was assigned to {station_name}."

    @staticmethod
    def train_astronauts(station: BaseStation, sessions_number: int) -> str:
        for astronaut in station.astronauts:
            for _ in range(sessions_number):
                astronaut.train()
        total_stamina = sum([a.stamina for a in station.astronauts])
        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."

    @staticmethod
    def retire_astronaut(station: BaseStation, astronaut_id_number: str) -> str:
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)
        if astronaut is None or astronaut.stamina == 100:
            return "The retirement process was canceled."
        station.astronauts.remove(astronaut)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        stations_sorted = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))

        result = (f"*Space Agency Up-to-Date Report*\n"
                  f"Total number of available astronauts: {len(self.astronauts)}\n"
                  f"**Stations count: {len(self.stations)}; Total available capacity: {sum(s.capacity for s in self.stations)}**\n")

        for station in stations_sorted:
            result += station.status() + "\n"

        return result
