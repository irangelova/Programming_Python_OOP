from project import Product


class Drink(Product):
    #def __int__(self, name: str, quantity: int = 10):
     #   super().__init__(name, quantity)

    def __init__(self, name: str):
        super().__init__(name, 10)
