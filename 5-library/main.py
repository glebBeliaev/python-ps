import sys


library: dict[str, str] = {
    "1984": "George Orwell",
    "Animal Farm": "George Orwell",
    "The Hobbit": "J.R.R. Tolkien",
    "The Lord of the Rings": "J.R.R. Tolkien",
    "Crime and Punishment": "Fyodor Dostoevsky",
}


# Базовый класс для всех ошибок программы
class LibraryError(Exception):
    pass


# Ошибка: команда не передана
class MissingActionError(LibraryError):
    pass


# Ошибка: команда неизвестна
class InvalidActionError(LibraryError):
    pass


# Ошибка: не передан текст для filter
class MissingFilterTextError(LibraryError):
    pass


# Ошибка: неверный параметр для sort
class InvalidSortParameterError(LibraryError):
    pass


try:
    if len(sys.argv) < 2:
        raise MissingActionError('Не передана команда. Используй: "filter" или "sort".')

    action = sys.argv[1]

    if action == "filter":
        if len(sys.argv) < 3:
            raise MissingFilterTextError(
                "Не передан текст фильтра. Укажи автора или название книги."
            )

        search_value = sys.argv[2].lower()

        filtered_books = filter(
            lambda item: search_value in item[0].lower()
            or search_value in item[1].lower(),
            library.items(),
        )

        result = list(map(lambda item: f"{item[0]} — {item[1]}", filtered_books))
        print(result)

    elif action == "sort":
        if len(sys.argv) < 3:
            raise InvalidSortParameterError(
                'Не передан параметр сортировки. Используй: "author" или "book".'
            )

        sort_by = sys.argv[2]

        if sort_by not in ("author", "book"):
            raise InvalidSortParameterError(
                'Передан кривой параметр сортировки. Используй: "author" или "book".'
            )

        books_list = list(map(lambda item: f"{item[0]} — {item[1]}", library.items()))

        if sort_by == "author":
            books_list.sort(key=lambda item: item.split(" — ")[1])
        else:
            books_list.sort(key=lambda item: item.split(" — ")[0])

        print(books_list)

    else:
        raise InvalidActionError(
            'Передана кривая команда. Используй: "filter" или "sort".'
        )

except LibraryError as e:
    print(f"Ошибка: {e}")
