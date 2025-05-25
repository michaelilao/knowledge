from abc import ABC, abstractmethod
from datetime import date

from Book import Book
from Member import Member


class Checkout():
    def __init__(self, book: Book, member: Member):
        self.checkoutDate = date.today()
        self.returnDate = None
        self.book = book
        self.member = member
        self.feeStrategy = SimpleFeeStrategy()

    def getReturnFee(self) -> int:
        fee = self.feeStrategy.calculateFee(self.book, self.member, self)
        return fee

    def returnBook(self):
        self.returnDate = date.today()

    def __str__(self):
        return f"{self.member.name} checked out {self.book.title} on {self.checkoutDate} and returned on {self.returnDate}"

    def __repr__(self):
        return self.__str__()


class FeeStrategy(ABC):
    @abstractmethod
    def calculateFee(self, book: Book, member: Member, checkout: Checkout):
        pass


class SimpleFeeStrategy():

    def calculateFee(self, book: Book, member: Member, checkout: Checkout):
        return 0
