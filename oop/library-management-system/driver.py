from LibrarySystem import LibrarySystem
from Book import Book, BookGenres
from Member import Member

ls = LibrarySystem()

pj = Book("Percy Jackson and the Lightning Theif",
          BookGenres.MYSTERY, "Rick Riordan")
lifeofpi = Book("Life of Pi", BookGenres.MYSTERY, "N/A")


ls.addBook(pj)
ls.addBook(lifeofpi)

michael = Member("Michael Ilao", "michaelilao@live.com")

books = ls.searchBooks("", "", BookGenres.MYSTERY)

isAvailable = ls.isBookAvailable(books[0])
print(books[0], isAvailable)


checkout = ls.checkoutBook(books[0], michael)
isAvailable = ls.isBookAvailable(books[0])
print(books[0], isAvailable)

print(checkout)
ls.processReturn(checkout)

isAvailable = ls.isBookAvailable(books[0])
print(books[0], isAvailable)
print(checkout)
