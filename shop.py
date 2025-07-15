from dataclasses import dataclass, field

class OrderNotPaid(Exception):
    pass

class UncorrectOrderStatus(Exception):
    pass

@dataclass
class Product:
    name: str
    price: int
    sku: int

    def __str__(self) -> str:
        return f'---\nТовар: {self.name}\nЦена: {self.price} руб\nАртикул: {self.sku}\n---\n'

@dataclass
class CartItem:
    product: Product
    quantity: int

    def __str__(self) -> str:
        return f'\n{self.product}Кол-во: {self.quantity}'

@dataclass
class ShoppingCart:
    cart_items: list[CartItem] | None 

    def add_cart_item(self, cartitem: CartItem) -> None:
        if self.cart_items: 
            self.cart_items.append(cartitem)

    def delete_cart_item(self, cartitem: CartItem) -> None:
        if self.cart_items:
            self.cart_items.remove(cartitem)
        self._sum_of_order -= cartitem.product.price * cartitem.quantity

    @property
    def sum_of_order(self) -> int:
        for item in self.cart_items:
            self._sum_of_order += item.quantity * item.product.price
        return self._sum_of_order
    
    def __str__(self) -> str:
        return '\nКорзина: ' + '\n'.join([str(item) for item in self.cart_items])

# TODO Добавить Enum в _order_status
class Order:
    order: list[CartItem]    
    _order_status: str = 'created'

    @property
    def order_status(self) -> str:
        return f'Статус заказа: {self._order_status}'

    def pay(self) -> None:
        self._order_status = 'paid'

    def ship(self) -> None:
        if self._order_status != 'paid':
            raise OrderNotPaid('Заказ не оплачен')
        self._order_status = 'shipped'

    def __str__(self) -> str:
        return '\nЗаказ:' + '\n'.join([str(item) for item in self.order]) + f'\nСтатус заказа: {self._order_status}'
        
if __name__ == "__main__":
    shampoo = Product('Head and Shoulders', 199, 123456)
    print(shampoo)

    bread = Product("Хлеб Harry\'s", 129, 987654)
    shampoo_item = CartItem(shampoo, 2)
    print(shampoo_item)

    bread_item = CartItem(bread, 1)

    shoppingcart = ShoppingCart()
    shoppingcart.add_cart_item(shampoo_item)
    shoppingcart.add_cart_item(bread_item)
    print(shoppingcart)
    print(f'Сумма заказа: {shoppingcart.sum_of_order} руб')
    shoppingcart.delete_cart_item(shampoo_item)
    print(shoppingcart)

    order = Order([shampoo_item, bread_item])
    print(order)
    print(order.order_status)
    order.pay()
    print(order.order_status)
    order.ship()
    print(order.order_status)     


# TODO Добавить Enum для статусов, переписать
