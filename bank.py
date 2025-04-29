from dataclasses import dataclass

@dataclass
class BankAccount:
    name: str
    _balance: int
    
    def __post_init__(self) -> None:
        if len(self.name) < 5 or self.name[0].isdigit():
            raise ValueError('Имя должно быть не менее 5 знаков и не может начинаться с цифры')

    @property
    def balance(self) -> int:
        return self._balance
    
    @balance.setter
    def balance(self, balance: int) -> None:
        if balance < 0:
            raise ValueError('Баланс не может быть отрицательным')
        self._balance = balance
    
    def deposit(self, amount: int) -> None:
        try:
            if amount < 0:
                raise ValueError('Пополнение не может быть отрицательным')
            self._balance += amount
        except ValueError as e:
            print(e)

    def withdraw(self, amount: int) -> None:
        try:
            if amount > self._balance:
                raise ValueError('Нельзя снять больше, чем есть на балансе')
            self._balance -= amount
        except ValueError as e:
            print(e)

    def __enter__(self) -> "BankAccount":
        print('Счет разблокирован')
        return self

    def __exit__(self, exc_type, exc_val, exc_cb) -> None:
        print('Счет заблокирован')

if __name__ == '__main__':
    with BankAccount("Alice", 1000) as account:
        account.deposit(500)
        account.withdraw(200)
        account.withdraw(2000)  # Ошибка: недостаточно средств
        try:
            account.balance = -100  # Ошибка: баланс не может быть отрицательным
        except ValueError:
            print('Баланс не может быть отрицательным')