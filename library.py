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
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, В наличии: {'да' if not self.is_checked_out else 'нет'}"
    
        
class Library:
    
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def list_available_books(self) -> list[Book]:
        return [book for book in self.books if not book.is_checked_out]
    
    def checkout_book(self, title: str) -> bool:
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                return True
        return False        
    
    def __str__(self) -> str:
        available_books = self.list_available_books()
        return '\n'.join(str(book) for book in available_books) if available_books else 'Нет доступных книг.' 
        
class User:

    def __init__(self, name: str, borrowed_books: list | None=None) -> None:
        if not self.validate_name(name):
            raise ValueError("Имя пользователя должно быть не менее 4 знаков и не может начинаться с цифры.")
        self.name = name
        self.borrowed_books = borrowed_books or []
    
    @staticmethod
    def validate_name(name: str) -> bool:
        return len(name) >= 4 and not name[0].isdigit()

    def borrow_book(self, library: Library, title: str) -> str:
        for book in library.list_available_books():
            if book.title == title:
                if book in self.borrowed_books:
                    return 'Вы уже взяли эту книгу'
                self.borrowed_books.append(book)
                book.is_checked_out = True
                return 'Книга выдана'
        return 'Нет доступных книг с таким названием'


    def list_borrowed_books(self) -> list:
        return [book for book in self.borrowed_books]
    
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
    for book in library.list_available_books():
        print(book)

    user = User("User")

    print("\nПользователь пытается взять книгу 'Идиот':")
    print(user.borrow_book(library, "Идиот")) 
    for book in user.list_borrowed_books():
        print(book)

    print("\nДоступные книги после того, как пользователь взял книгу:")
    for book in library.list_available_books():
        print(str(book))

    print("\nПользователь пытается взять книгу 'Преступление и наказание':")
    print(user.borrow_book(library, "Преступление и наказание"))  
    for book in user.list_borrowed_books():
        print(book)

    print(user.borrow_book(library, "Идиот"))  
    for book in user.list_borrowed_books():
        print(book)

    print("\nСписок всех взятых книг пользователем:")
    for book in user.list_borrowed_books():
        print(book)

if __name__ == "__main__":
    test_library_system()


