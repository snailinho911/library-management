import json
import os
from typing import List
from source.book import Book


class LibraryStorage:
    """
    Управляет загрузкой и сохранением книг в файл данных.
    """

    def __init__(self, data_file: str) -> None:
        self.data_file: str = data_file

    def load_books(self) -> List[Book]:
        """
        Загружает книги из файла.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return [Book.from_dict(item) for item in data]
            except (IOError, json.JSONDecodeError) as e:
                print(f"Ошибка загрузки данных из файла: {e}")
                return []

    def save_books(self, books: List[Book]) -> None:
        """
        Сохраняет книги в файл.
        """
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Ошибка сохранения данных в файл: {e}")