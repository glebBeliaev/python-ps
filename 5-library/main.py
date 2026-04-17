library: dict[str, str] = {}

library = {
    "1984": "George Orwell",
    "Animal Farm": "George Orwell",
    "The Hobbit": "J.R.R. Tolkien",
    "The Lord of the Rings": "J.R.R. Tolkien",
    "Crime and Punishment": "Fyodor Dostoevsky",
}

print("Все книги:", library)

unique_authors: set[str] = set()

for author in library.values():
    unique_authors.add(author)

print("Уникальные авторы: ", unique_authors)
