class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @property
    def price(self) -> int:
        return self._price
    
    @price.setter
    def price(self, price: int) -> None:
        if price < 0:
            raise ValueError('Цена не может быть отрицательным')
        self._price = price

    def __str__(self) -> str:
        return f'Название: {self.name}, Цена: {self.price} руб.'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MenuItem):
            return NotImplemented
        return self.name == other.name and self.price == other.price
    
class Order:
    def __init__(self, cafe: "Cafe") -> None:
        self.items: list[MenuItem] = []
        self.cafe = cafe

    def add_item(self, item: MenuItem) -> None:
        try:
            if item not in self.cafe.menu:
                raise ValueError('Такой позиции нет в меню')
            self.items.append(item)
        except ValueError as e:
            raise ValueError(e)
        
    def total_price(self) -> float:
        return sum(item.price for item in self.items)
    
    def __str__(self) -> str:
        return '\n'.join([str(item) for item in self.items]) + f"\nИтого: {self.total_price()} руб." 

class Cafe:
    def __init__(self) -> None:
        self.menu: list[MenuItem] = []
        self.orders: list[Order] = [] 
    
    def add_menu_item(self, item: MenuItem) -> None:
        self.menu.append(item)

    def create_order(self) -> Order:
        return Order(self)

    def add_order(self, order: Order) -> None:
        self.orders.append(order)

    def list_menu(self) -> list[str]:
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

    order1 = cafe.create_order()
    order1.add_item(MenuItem('Шашлык', 100.00))
    order1.add_item(MenuItem('Чай', 30.00))

    cafe.add_order(order1)

    print("\nСозданный заказ:")
    print(order1)

    order2 = cafe.create_order()
    # order2.add_item(MenuItem('Люля-кебаб', 250.00))
    cafe.add_menu_item(MenuItem('Салфетка', -1.00))
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