from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    year: int
    _available: bool = True

    def __post_init__(self) -> None: 
        if len(self.title.strip()) < 3 or len(self.author) < 3 or self.year < 1450:
            raise ValueError('Некорректные данные книги')

    @property
    def available(self) -> bool:
        return self._available

    @available.setter
    def available(self, available: bool) -> None:
        self._available = available

    def __str__(self) -> str:
        return f'{self.title}, {self.author}, {self.year}'

@dataclass
class Library:
    library: list = field(default_factory=list) 
    
    def add_book(self, book: Book) -> None:
        self.library.append(book)
        print(f'Книга {book.title} добавлена')
        
    def remove_book(self, title: str) -> None:
        for book in self.library:
            if book.title == title:
                self.library.remove(book)
                print(f'Книга {title} удалена')
                return
        print(f'Книга {title} не найдена')

    def find_book(self, title: str) -> None:   
        for book in self.library:
            if title == book.title:
                return f'Книга {book.title} есть в библиотеке'        
        raise ValueError(f"Книга {title} отсутствует.")
    
    def list_books(self) -> str:
        return [book for book in self.library]
        
    def __str__(self) -> str:
        return '\n'.join(str(book) for book in self.list_books())        

@dataclass
class User:
    name: str
    borrowed_books: list = field(default_factory=list)

    def borrow_book(self, library: Library, title: str) -> None:
        for book in library.list_books():
            if book.title == title:
                if book in self.borrowed_books:               
                    return f'Вы уже брали книгу {title}'
                if not book.available:
                    return f'Книгу {title} уже взяли'
                self.borrowed_books.append(book)
                book._available = False
                return f'Книга {title} выдана'
        return f'Книга {title} отсутствует в библиотеке'

    def return_book(self, library: Library, title: str) -> None:
        for book in library.list_books():
            if book.title == title:
                if book in self.borrowed_books:               
                    self.borrowed_books.remove(book)
                    book._available = True
                    return f'Вы вернули книгу {title} в библиотеку'
            else:
                return f'Вы не брали книгу {title}'
        return f'Книга {title} отсутствует в библиотеке'

    def __str__(self) -> str:
        return '\n'.join(str(book) for book in self.borrowed_books)

b1 = Book('Братья Карамазовы', 'Ф. М. Достоевский', 1867)
b2 = Book('Война и мир', 'Л. Н. Толстой', 1869)
print(b1)

library = Library()
library.add_book(b1)
library.add_book(b2)
print(library)
try:
    library.find_book('Гранатовый браслет')
except ValueError as e:
    print(e)
try:
    print(library.find_book('Братья Карамазовы'))
except ValueError as e:
    print(e)

library.remove_book('Братья Карамазовы')

try:
    print(library.find_book('Братья Карамазовы'))
except ValueError as e:
    print(e)

library.remove_book('Архипелаг ГУЛАГ')
print(f'\n{library}\n')

user = User('Alex')
print(user.borrow_book(library, 'Война и мир'))
print('Список выданных книг:')
print(user.borrowed_books)

print(user.return_book(library, 'Война и мир'))
print(user.borrowed_books)