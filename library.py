"""
🔹 Задача: Мини-библиотека

Создай три класса:
1. Book

Представляет книгу.

Атрибуты:

    title (название)

    author (автор)

    year (год издания)

    is_checked_out (флаг, выдана ли книга; по умолчанию — False)

Методы:

    __str__: возвращает строку вида "Название: ..., Автор: ..., Год: ..., В наличии: да/нет"

2. Library

Представляет библиотеку, в которой хранятся книги.

Атрибуты:

    books — список объектов Book

Методы:

    add_book(book: Book) — добавляет книгу в библиотеку.

    list_available_books() — возвращает список только доступных книг.

    checkout_book(title: str) — "выдаёт" книгу (меняет is_checked_out на True, если книга есть и не выдана).

3. User

Представляет пользователя, который может брать книги.

Атрибуты:

    name

    borrowed_books — список книг, взятых этим пользователем.

Методы:

    borrow_book(library: Library, title: str) — пытается взять книгу из библиотеки.

    list_borrowed_books() — список всех взятых книг.
"""

class Book:
    
    def __init__(
            self, 
            title: str, 
            author: str, 
            year: int, 
            is_checked_out: bool=False) -> None:
        
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out
    
    def __str__(self) -> str:
        if not self.is_checked_out:
            flag_checked_out = 'да'
        else:
            flag_checked_out = 'нет'
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, В наличии: {flag_checked_out}"
        
class Library:
    
    def __init__(self) -> None:
        self.books = list()
        self.available_books = list()

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def list_available_books(self) -> list:
        available_books = []
        for book in self.books:
            if not book.is_checked_out:
                available_books.append(str(book))
        return available_books

    
    def checkout_book(self, title: str) -> None:

        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                return f'Книга {book.title} выдана'
            
        return 'Книги сейчас нет в библиотеке'         
    
    def __str__(self) -> str:
        list_available_books = [book for book in self.list_available_books()]
        if not list_available_books:
            return 'Нет доступных книг.'
        return '\n'.join(list_available_books)


class User:

    def __init__(self, name: str, borrowed_books: list=None) -> None:
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
    
    def borrow_book(self, library: Library, title: str) -> None:
        for book in library.list_available_books():
            if book.title == title:
                if book in self.borrowed_books:
                    return 'Вы уже взяли эту книгу'
                self.borrowed_books.append(book)    
                library.checkout_book(title)
                return 'Книга выдана'
        return 'Нет доступных книг с таким названием'

    def list_borrowed_books(self) -> list:
        borrowed_books = []
        for book in self.borrowed_books:
            borrowed_books.append(str(book))
        return borrowed_books
    
    def __str__(self) -> str:
        if not self.borrowed_books:
            return 'Вы не брали книги в библиотеке'
        return '\n'.join([str(book) for book in self.borrowed_books])            

def test_library_system():
    book1 = Book("Братья Карамазовы", "Федор Достоевский", 1880)
    book2 = Book("Идиот", "Федор Достоевский", 1869)
    book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Доступные книги в библиотеке:")
    print(library.list_available_books())

    user = User("User")

    print("\nПользователь пытается взять книгу 'Идиот':")
    print(user.borrow_book(library, "Идиот")) 
    print(user.list_borrowed_books())

    print("\nДоступные книги после того, как пользователь взял книгу:")
    print(library.list_available_books())

    print("\nПользователь пытается взять книгу 'Преступление и наказание':")
    print(user.borrow_book(library, "Преступление и наказание"))  
    print(user.list_borrowed_books())

    print(user.borrow_book(library, "Идиот"))  
    print(user.list_borrowed_books())

    print("\nСписок всех взятых книг пользователем:")
    print(user.list_borrowed_books())

if __name__ == "__main__":
    test_library_system()


