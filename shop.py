from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: int
    sku: int

    def __str__(self) -> str:
        return f'---\nТовар: {self.name}\nЦена: {self.price} руб\nАртикул: {self.sku}\n'

@dataclass
class CartItem:
    product: Product
    quantity: int

    def __str__(self) -> str:
        return f'{self.product}Кол-во: {self.quantity}\n---\n'

@dataclass
class ShoppingCart:
    shoppingcart: list[CartItem] = field(default_factory=list)
    sum_of_order: int = 0

    def add_cart_item(self, cartitem: CartItem) -> None:
       self.shoppingcart.append(cartitem)

    def delete_cart_item(self, cartitem: CartItem) -> None:
       self.shoppingcart.remove(cartitem)

    def sum_of_order(self) -> int:
        for item in self.shoppingcart:
            self.sum_of_order += item.quantity * item.price
        return f'Сумма заказа: {self.sum_of_order}'

@dataclass
class Order:
    order: list[CartItem]
    _order_status: str

    @property
    def order_status(self) -> str:
        return self._order_status

    @order_status.setter
    def order_status(self, status: str) -> None:
        self._order_status = status

    def pay(self):
        pass

    def ship(self):
        pass
        
    def validate(self):
        pass


if __name__ == "__main__":
    shampoo = Product('Head and Shoulders', 199, 123456)
    print(shampoo)

    shampoo_item = CartItem(shampoo, 2)
    print(shampoo_item)

    shoppingcart = ShoppingCart()
    shoppingcart.add_cart_item(shampoo_item)
    print(shoppingcart) 
    print(shoppingcart.sum_of_order())
    shoppingcart.delete_cart_item(shampoo_item)
    print(shoppingcart)