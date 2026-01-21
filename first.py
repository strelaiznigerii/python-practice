import datetime

# Словари — это отлично, оставляем их для масштабируемости
DEFAULT_GET = {
    'desc': 'Описание', 
    'category': 'Категория [expenses]', 
    'subcategory': 'Подкатегория [products]', 
    'amount': 'Сумма', 
    'account': 'Актив [assets]', 
    'subaccount': 'Счет списания [salarycard]'
}

DEFAULT_VALUES = {
    'category': 'expenses', 
    'subcategory': 'products', 
    'account': 'assets', 
    'subaccount': 'salarycard'
}

def get_input(key: str) -> str:
    # Берем ввод пользователя один раз
    user_input = input(f"{DEFAULT_GET[key]}: ").strip()
    # Возвращаем ввод или дефолтное значение (если ввод пустой)
    return user_input or DEFAULT_VALUES.get(key, "")

def add_entry() -> None:
    # Теперь ввод данных проходит линейно и быстро
    desc = input(f"{DEFAULT_GET['desc']}: ")
    category = get_input('category')
    subcategory = get_input('subcategory')
    amount = input(f"{DEFAULT_GET['amount']}: ")
    account = get_input('account')
    subaccount = get_input('subaccount')

    # Формирование записи
    entry = (
        f"{datetime.date.today().strftime('%Y/%m/%d')} {desc}\n"
        f"    {category}:{subcategory}      {amount} RUB\n"
        f"    {account}:{subaccount}\n\n"
    )

    with open("finance.ledger", "a", encoding="utf-8") as f:
        f.write(entry)
    print("✅ Запись добавлена!")

if __name__ == "__main__":
    add_entry()
