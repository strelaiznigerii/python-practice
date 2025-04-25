class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        if price <= 0:
            raise ValueError('Цена не может быть отрицательной')
        self.price = price

    def __str__(self) -> str:
        return f'Название: {self.name}, Цена: {self.price} руб.'

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
        return Order()

    def add_order(self, order: Order) -> None:
        self.orders.append(order)

    def list_menu(self) -> list:
        return [str(item) for item in self.menu]
    
    def __str__(self) -> str:
        return '\n'.join(self.list_menu())

def test_cafe():
    cafe = Cafe()

    cafe.add_menu_item(MenuItem('Шашлык', 100.00))
    cafe.add_menu_item(MenuItem('Суп', 50.00))
    cafe.add_menu_item(MenuItem('Чай', 30.00))

    print("Меню кафе:")
    for item in cafe.list_menu():
        print(item)

    order1 = Cafe.create_order()
    order1.add_item(MenuItem('Шашлык', 100.00))
    order1.add_item(MenuItem('Чай', 30.00))

    cafe.add_order(order1)

    print("\nСозданный заказ:")
    print(order1)

    order2 = Cafe.create_order()
    cafe.add_menu_item(MenuItem('Люля-кебаб', 250.00))
    
    order2.add_item(MenuItem('Суп', 50.00))
    order2.add_item(MenuItem('Люля-кебаб', 250.00))

    cafe.add_order(order2)

    print("\nОбновленное меню кафе:")
    for item in cafe.list_menu():
        print(item)

    print("\nСозданный заказ:")
    print(order2)

    print(f"\nВсего заказов в кафе: {len(cafe.orders)}")

if __name__ == '__main__':
    test_cafe()