from enum import Enum


class BookGenres(Enum):
    MYSTERY = 1
    ROMANCE = 2
    SCIFI = 3
    NONFICTION = 4


class Book():
    def __init__(self, title: str, genre: BookGenres, author: str):
        self.title = title
        self.genre = genre
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return self.__str__()

# Could have a factory pattern for creating books
