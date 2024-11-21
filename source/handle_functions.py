from source.library import Library


def add_book(library: Library) -> None:
    try:
        title = input("Введите название книги: ").strip()
        author = input("Введите автора книги: ").strip()
        year_input = input("Введите год издания: ").strip()
        if not year_input.isdigit():
            raise ValueError("Год должен быть числом.")
        year = int(year_input)
        library.add_book(title, author, year)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")


def delete_book(library: Library) -> None:
    try:
        book_id_input = input("Введите ID книги для удаления: ").strip()
        if not book_id_input.isdigit():
            raise ValueError("ID должен быть числом.")
        book_id = int(book_id_input)
        library.delete_book(book_id)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")


def search_books(library: Library) -> None:
    try:
        field = input("Введите поле (title, author, year): ").strip()
        if field not in ["title", "author", "year"]:
            raise ValueError("Недопустимое поле для поиска.")
        value = input(f"Введите значение для {field}: ").strip()
        if field == "year" and not value.isdigit():
            raise ValueError("Год должен быть числом.")
        results = library.search_books(**{field: int(value) if field == "year" else value})
        library.display_books(results)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")


def display_books(library: Library) -> None:
    library.display_books()


def change_status(library: Library) -> None:
    try:
        book_id_input = input("Введите ID книги для изменения статуса: ").strip()
        if not book_id_input.isdigit():
            raise ValueError("ID должен быть числом.")
        book_id = int(book_id_input)
        status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
        if status not in ["в наличии", "выдана"]:
            raise ValueError("Статус должен быть 'в наличии' или 'выдана'.")
        library.change_status(book_id, status)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")


def exit_program(*args) -> None:
    print("Спасибо за использование библиотеки!")
    exit()