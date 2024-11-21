import unittest
from unittest.mock import MagicMock
from source.library import Library
from source.book import Book


class TestLibrary(unittest.TestCase):  # Создаем класс для тестирования библиотеки
    def setUp(self) -> None:  # Метод для подготовки данных перед каждым тестом
        # Создаем мок для хранилища книг
        self.mock_storage = MagicMock()
        self.mock_storage.load_books.return_value = []  # Загружаем пустое хранилище для начала
        self.library = Library(self.mock_storage)  # Создаем объект библиотеки с мок-данными

    def test_add_book(self):  # Тестируем добавление книги в библиотеку
        self.library.add_book("Test Title", "Test Author", 2023)  # Добавляем книгу
        self.assertEqual(len(self.library.books), 1)  # Проверяем, что в библиотеке 1 книга
        self.assertEqual(self.library.books[0].title, "Test Title")  # Проверяем, что книга имеет правильное название

    def test_delete_book(self):  # Тестируем удаление книги из библиотеки
        # Создаем книгу и добавляем её в библиотеку
        book = Book(1, "Test Title", "Test Author", 2023)
        self.library.books.append(book)
        # Удаляем книгу по ID
        self.library.delete_book(1)
        self.assertEqual(len(self.library.books), 0)  # Проверяем, что книги больше нет в библиотеке

    def test_search_books(self):  # Тестируем поиск книг в библиотеке
        # Создаем книгу и добавляем её в библиотеку
        book = Book(1, "Python Basics", "Author A", 2021)
        self.library.books.append(book)
        # Ищем книгу по названию
        result = self.library.search_books(title="Python Basics")
        self.assertEqual(len(result), 1)  # Проверяем, что нашли 1 книгу

    def test_change_status(self):  # Тестируем изменение статуса книги
        # Создаем книгу и добавляем её в библиотеку
        book = Book(1, "Python Basics", "Author A", 2021)
        self.library.books.append(book)
        # Меняем статус книги на "выдана"
        self.library.change_status(1, "выдана")
        self.assertEqual(book.status, "выдана")  # Проверяем, что статус изменен на "выдана"


if __name__ == "__main__":
    unittest.main()
