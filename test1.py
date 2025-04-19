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

    # def __str__(self) -> str:
    #     return '\n'.join(self.books)

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def list_available_books(self) -> list:
        for book in self.books:
            if book.is_checked_out == False:
                self.available_books.append(book)
        return self.available_books
    
    def checkout_book(self, title: str) -> None:
        for book in self.books:
            if book.title in self.books and book.is_checked_out == False:
                book.is_checked_out = True
        
class User:
    def __init__(self, name: str, borrowed_books: list) -> None:
        self.name = name
        self.borrowed_books = borrowed_books
    
    def borrow_book(self, library: Library, title: str) -> None:
        if title in library.list_available_books():
            pass

    def list_borrowed_books(self) -> list:
        pass


if __name__ == "__main__":
    b1 = Book('Братья Карамазовы', 'Ф. М. Достоевский', 1867)
    print(b1)
    b2 = Book('Идиот', 'Ф. М. Достоевский', 1867)
    print(b2)
    
    l1 = Library()
    l1.add_book(b1)
    l1.add_book(b2)
    print(l1.list_available_books())

