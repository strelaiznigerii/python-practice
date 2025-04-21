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
        if self.is_checked_out == False:
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
        print(available_books)
        return available_books

    
    def checkout_book(self, title: str) -> None:
        count_checked_books = 0

        for book in self.books:
            if book.title == title and book.is_checked_out == False:
                book.is_checked_out = True
                count_checked_books += 1
                return f'Книга {book.title} выдана'

        if count_checked_books == 0:
            return 'Книги сейчас нет в библиотеке'         
    
    def __str__(self) -> str:
        list_available_books = [str(book) for book in self.list_available_books()]
        if not list_available_books:
            return 'Нет доступных книг.'
        return '\n'.join(list_available_books)


class User:

    def __init__(self, name: str, borrowed_books: list=None) -> None:
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books is not None else {}
    
    def borrow_book(self, library: Library, title: str) -> None:
        for book in library.list_available_books():
            if book.title in library and book.is_checked_out == False:
                self.borrowed_books.append(book)
            else:
                print('Вы не можете взять книгу')

    def list_borrowed_books(self) -> list:
        return self.borrowed_books
    
    def __str__(self) -> str:
        return f'{self.borrowed_books}'


if __name__ == "__main__":
    b1 = Book('Братья Карамазовы', 'Ф. М. Достоевский', 1867)
    print(b1)
    b2 = Book('Идиот', 'Ф. М. Достоевский', 1867)
    print(b2)
    
    l1 = Library()
    l1.add_book(b1)
    l1.add_book(b2)
    print(l1)
    print(l1.checkout_book('Братья Карамазовы'))

    print(l1.list_available_books())
    # print(str(b1))
    # u = User('User1')
    # print(User.name)

