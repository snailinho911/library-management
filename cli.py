from source.storage import LibraryStorage
from source.library import Library
from source.handle_functions import add_book, delete_book, search_books, display_books, change_status, exit_program


def run_cli() -> None:
    """
    Интерфейс командной строки.
    """
    library = Library(LibraryStorage("data/library.json"))

    actions = {
        "1": add_book,
        "2": delete_book,
        "3": search_books,
        "4": display_books,
        "5": change_status,
        "6": exit_program,
    }

    while True:
        print("\nДобро пожаловать в библиотечную систему!")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Введите номер действия: ").strip()
        action = actions.get(choice)

        if action:
            try:
                action(library)
            except Exception as e:
                print(f"Произошла ошибка при выполнении операции: {e}")
        else:
            print("Ошибка: Неверный выбор.")


if __name__ == "__main__":
    run_cli()
