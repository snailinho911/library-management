import unittest
from unittest.mock import patch, MagicMock
from cli import run_cli
from source.library import Library

class TestCLI(unittest.TestCase):  # Создаем класс для тестирования CLI
    # Патчим функцию input, чтобы она возвращала заранее заданные значения по очереди
    @patch("builtins.input", side_effect=["1", "Test Title", "Test Author", "2023", "6"])
    @patch("builtins.print")  # Патчим print, чтобы проверить его вызовы
    def test_add_book(self, mock_print, mock_input):
        # Настройка мок-объекта для хранилища
        mock_storage = MagicMock()  # Создаем мок-объект для хранилища
        mock_storage.load_books.return_value = []  # Когда вызывается load_books, возвращаем пустой список
        library = Library(mock_storage)  # Создаем объект библиотеки, передавая мок-хранилище

        # Патчим класс Library в cli.py, чтобы использовать наш мок-объект
        with patch("cli.Library", return_value=library):
            # Ожидаем, что при вызове run_cli() будет вызвано завершение программы (SystemExit)
            with self.assertRaises(SystemExit):
                run_cli()  # Запускаем CLI

        # Проверяем, что книга была добавлена в библиотеку
        self.assertEqual(len(library.books), 1)  # Должна быть добавлена одна книга
        # Проверяем, что выводился правильный текст о добавленной книге
        mock_print.assert_any_call("Книга 'Test Title' добавлена с ID 1.")

if __name__ == "__main__":
    unittest.main()
