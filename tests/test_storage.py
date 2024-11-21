import unittest
import os
from source.storage import LibraryStorage
from source.book import Book


class TestLibraryStorage(unittest.TestCase):  # Создаем класс для тестирования хранилища книг
    TEST_FILE = "test_data.json"  # Определяем имя тестового файла

    def setUp(self) -> None:  # Метод для подготовки данных перед каждым тестом
        self.storage = LibraryStorage(self.TEST_FILE)  # Создаем объект хранилища с тестовым файлом

    def tearDown(self) -> None:  # Метод для очистки после выполнения теста
        # Удаляем тестовый файл, если он был создан
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_save_and_load_books(self):  # Тестируем сохранение и загрузку книг
        book = Book(1, "Test Title", "Test Author", 2023)  # Создаем объект книги
        self.storage.save_books([book])  # Сохраняем книгу в хранилище
        books = self.storage.load_books()  # Загружаем книги из хранилища
        self.assertEqual(len(books), 1)  # Проверяем, что в хранилище только 1 книга
        self.assertEqual(books[0].title, "Test Title")  # Проверяем, что загруженная книга имеет правильное название


if __name__ == "__main__":
    unittest.main()
