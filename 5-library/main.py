import sys

library: dict[str, str] = {
    "1984": "George Orwell",
    "Animal Farm": "George Orwell",
    "The Hobbit": "J.R.R. Tolkien",
    "The Lord of the Rings": "J.R.R. Tolkien",
    "Crime and Punishment": "Fyodor Dostoevsky",
}

action = sys.argv[1]

if action == "filter":
    # Например: George Orwell
    search_value = sys.argv[2].lower()

    filtered_books = filter(
        lambda item: search_value in item[0].lower() or search_value in item[1].lower(),
        library.items(),
    )

    result = list(map(lambda item: f"{item[0]} — {item[1]}", filtered_books))

    print(result)

elif action == "sort":
    # Например: author или book
    sort_by = sys.argv[2]

    books_list = list(map(lambda item: f"{item[0]} — {item[1]}", library.items()))

    if sort_by == "author":
        books_list.sort(key=lambda item: item.split(" — ")[1])

    elif sort_by == "book":
        books_list.sort(key=lambda item: item.split(" — ")[0])

    print(books_list)
