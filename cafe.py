class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'Название: {self.name}, Цена: {self.price} руб.'
    
class Order:
    def __init__(self) -> None:
        self.items = list()

class Cafe:
    pass
