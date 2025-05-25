from abc import ABC, abstractmethod
from datetime import date
from typing import List

from Book import Book, BookGenres
from Member import Member
from Checkout import Checkout


class LibrarySystem():
    _instance = None

    def __init__(self):
        if LibrarySystem._instance is not None:
            raise Exception("Class is singleton")
        else:
            LibrarySystem._instance = self
            self.books: List[Book] = []
            self.checkouts: List[Checkout] = []

    def get_instance():
        if LibrarySystem._instance is None:
            LibrarySystem()
        return LibrarySystem._instance

    def addBook(self, book: Book):
        self.books.append(book)

    def searchBooks(self, title: str, author: str, genre: BookGenres) -> List[Book]:
        return self.books

    def isBookAvailable(self, bookToCheck: Book) -> bool:
        bookCheckedOut = next((c for c in self.checkouts if c.book.title ==
                              bookToCheck.title and c.returnDate is None), None)

        if bookCheckedOut is None:
            return True
        else:
            return False

    def checkoutBook(self, book: Book, member: Member) -> Checkout:
        c = Checkout(book, member)
        self.checkouts.append(c)
        return c

    def processReturn(self, checkout: Checkout):
        fee = checkout.getReturnFee()
        # pay fee
        print("You owe $" + str(fee))
        checkout.returnBook()
