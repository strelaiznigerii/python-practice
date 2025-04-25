class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'Название: {self.name}, Цена: {self.price} руб.'
    # TODO: add raise for price <= 0

class Order:
    def __init__(self) -> None:
        self.items = list()

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def total_price(self) -> float:
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price
    
    def __str__(self) -> str:
        return '\n'.join([str(item) for item in self.items]) + f"\nИтого: {self.total_price()} руб." 

class Cafe:
    def __init__(self) -> None:
        self.menu = list()
        self.orders = list()

    def add_menu_item(self, item: MenuItem):
        self.menu.append(item)

    @staticmethod
    def create_order() -> Order:
        order = Order()

    def add_order(self, order: Order) -> None:
        self.orders.append(order)

    def list_menu(self) -> list:
        return [item for item in self.menu]
    
    def __str__(self) -> str:
        return '\n'.join(self.list_menu())

a1 = MenuItem('шашлык', 100.00)
print(a1)
o1 = Order()
o1.add_item(a1) 
print(o1)