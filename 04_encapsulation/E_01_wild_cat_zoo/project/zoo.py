from typing import List, Union

from project import Animal
from project import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget <= price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name) -> str:
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        # if worker_name in self.workers:
        #     self.workers.remove(worker_name)
        #     return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum(worker.salary for worker in self.workers)
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_animal_costs = sum(animal.money_for_care for animal in self.animals)
        if total_animal_costs <= self.__budget:
            self.__budget -= total_animal_costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")

    def workers_status(self) -> str:
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

    @staticmethod
    def __print_status(all_zoo_animals: List[Union[Animal, Worker]], *args):
        elements = {arg: [] for arg in args}  # {Lion: [...], Tiger: [...]}
        for element in all_zoo_animals:
            elements[element.__class__.__name__].append(repr(element))

        result = [f"You have {len(all_zoo_animals)} {str(all_zoo_animals[0].__class__.__bases__[0].__name__).lower()}s"]
        for key in args:
            value = elements[key]
            result.append(f"----- {len(value)} {key}s:")
            result.extend(value)

        return "\n".join(result)


