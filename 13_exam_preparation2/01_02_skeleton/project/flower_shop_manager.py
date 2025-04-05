from typing import List, Type

from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANTS: List[Type[BasePlant]] = [Flower, LeafPlant]
    VALID_CLIENTS: List[Type[BaseClient]] = [RegularClient, BusinessClient]

    def __init__(self):
        self.income: float = 0.0
        self.plants: List[BasePlant] = []
        self.clients: List[BaseClient] = []
        self.__total_orders_count = 0

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str) -> str:
        plant_class = next((p for p in self.VALID_PLANTS if p.__name__ == plant_type), None)
        if plant_class is None:
            raise ValueError("Unknown plant type!")

        plant = plant_class(plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str) -> str:
        client_class = next((c for c in self.VALID_CLIENTS if c.__name__ == client_type), None)
        if client_class is None:
            raise ValueError("Unknown client type!")

        if any(c.phone_number == client_phone_number for c in self.clients):
            raise ValueError("This phone number has been used!")

        client = client_class(client_name, client_phone_number)
        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int) -> str:
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")

        plants = [p for p in self.plants if p.name == plant_name]
        if not plants:
            raise ValueError("Plants not found!")

        if len(plants) < plant_quantity:
            return "Not enough plant quantity."

        total_sum = next((p.price for p in plants), None) * plant_quantity
        total_sum = total_sum - client.discount * total_sum / 100
        self.income += total_sum
        self.plants = self.plants[plant_quantity-1:]

        client.update_total_orders()
        client.update_discount()
        self.__total_orders_count += 1

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {total_sum:.2f}"

    def remove_plant(self, plant_name: str) -> str:
        plants = [plant for plant in self.plants if plant.name == plant_name]
        if not plants:
            return "No such plant name."
        plant = plants[0]
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self) -> str:
        clients = [c for c in self.clients if c.total_orders == 0]
        [self.clients.remove(c) for c in clients]
        return f"{len(clients)} client/s removed."

    def shop_report(self) -> str:
        unsold_flowers = {}
        for plant in self.plants:
            if plant.name not in unsold_flowers:
                unsold_flowers[plant.name] = len([p for p in self.plants if p.name == plant.name])

        unsold_plants_sorted = sorted(unsold_flowers.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        clients_sorted = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))

        result = (f"~Flower Shop Report~\n"
                  f"Income: {self.income:.2f}\n"
                  f"Count of orders: {self.__total_orders_count}\n"
                  f"~~Unsold plants: {sum(unsold_flowers.values())}~~\n")

        for plant_name, count in unsold_plants_sorted:
            result += f"{plant_name}: {count}\n"

        result += f"~~Clients number: {len(clients_sorted)}~~\n"
        for client in clients_sorted:
            result += client.client_details() + "\n"

        return result
