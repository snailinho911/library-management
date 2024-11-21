import unittest
from source.book import Book


class TestBook(unittest.TestCase):  # Создаем класс для тестирования класса Book
    def test_to_dict(self):  # Тестируем метод to_dict, который преобразует объект в словарь
        # Создаем экземпляр книги с тестовыми данными
        book = Book(book_id=1, title="Test Title", author="Test Author", year=2023)
        book_dict = book.to_dict()  # Преобразуем объект книги в словарь
        # Проверяем, что поля в словаре соответствуют ожидаемым
        self.assertEqual(book_dict["id"], 1)
        self.assertEqual(book_dict["title"], "Test Title")
        self.assertEqual(book_dict["author"], "Test Author")
        self.assertEqual(book_dict["year"], 2023)
        self.assertEqual(book_dict["status"], "в наличии")  # Проверяем, что статус по умолчанию - "в наличии"

    def test_from_dict(self):  # Тестируем метод from_dict, который создает объект книги из словаря
        # Создаем словарь с данными для книги
        data = {
            "id": 1,
            "title": "Test Title",
            "author": "Test Author",
            "year": 2023,
            "status": "в наличии",
        }
        book = Book.from_dict(data)  # Создаем объект книги из словаря
        # Проверяем, что поля объекта книги соответствуют данным из словаря
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, "в наличии")  # Проверяем, что статус корректно установлен


if __name__ == "__main__":
    unittest.main()
