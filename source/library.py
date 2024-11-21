from typing import List, Optional
from source.book import Book
from source.storage import LibraryStorage


class Library:
    """
    Основной класс для работы с библиотекой.
    """

    def __init__(self, storage: LibraryStorage) -> None:
        self.storage = storage
        self.books: List[Book] = self.storage.load_books()
        self.next_id: int = max((book.id for book in self.books), default=0) + 1

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в библиотеку.
        """
        new_book = Book(book_id=self.next_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.next_id += 1
        self.storage.save_books(self.books)
        print(f"Книга '{title}' добавлена с ID {new_book.id}.")

    def delete_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по ID.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.storage.save_books(self.books)
                print(f"Книга с ID {book_id} удалена.")
                return
        print(f"Ошибка: Книга с ID {book_id} не найдена.")

    def search_books(self, **kwargs) -> List[Book]:
        """
        Ищет книги по заданным параметрам.
        """
        results = self.books
        for key, value in kwargs.items():
            if key == "year":
                value = int(value)
            results = [book for book in results if getattr(book, key) == value]
        return results

    def display_books(self, books: Optional[List[Book]] = None) -> None:
        """
        Отображает список книг.
        """
        if books is None:
            books = self.books
        if not books:
            print("Книги не найдены.")
            return
        print(f"{'ID':<5} {'Название':<30} {'Автор':<20} {'Год':<6} {'Статус':<10}")
        print("-" * 75)
        for book in books:
            print(f"{book.id:<5} {book.title:<30} {book.author:<20} {book.year:<6} {book.status:<10}")

    def change_status(self, book_id: int, new_status: str) -> None:
        """
        Изменяет статус книги по ID.
        """
        if new_status not in ["в наличии", "выдана"]:
            print("Ошибка: Некорректный статус. Используйте 'в наличии' или 'выдана'.")
            return
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.storage.save_books(self.books)
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
                return
        print(f"Ошибка: Книга с ID {book_id} не найдена.")
