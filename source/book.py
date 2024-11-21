from typing import Dict


class Book:
    """
    Класс Book представляет книгу в библиотеке.
    """

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии") -> None:
        self.id: int = book_id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

    def to_dict(self) -> Dict:
        """
        Преобразует объект Book в словарь для сохранения в JSON.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """
        Создает объект Book из словаря.
        """
        return Book(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"]
        )
