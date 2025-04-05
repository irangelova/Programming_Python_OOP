from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    SPECIALIZATION = "EngineerAstronaut"
    STAMINA = 80

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALIZATION, self.STAMINA)

    def train(self) -> None:
        if self.stamina + 5 > 100:
            self.stamina = 100
        else:
            self.stamina += 5
