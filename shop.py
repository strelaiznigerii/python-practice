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

class ShoppingCart:
    shoppingcart: list[CartItem] = field(default_factory=list)

    def add_cart_item(self, cartitem: CartItem) -> None:
       self.shoppingcart.append(cartitem)

    def delete_cart_item(self, cartitem: CartItem):
        self.shoppingcart.remove(cartitem)

    def sum_of_order(self):
        pass

@dataclass
class Order:
    order: list[CartItem]
    _order_status: str

    @property
    def order_status(self) -> None:
        pass
    @order_status.setter
    def order_status(self) -> None:
        pass

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
