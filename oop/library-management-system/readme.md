# Library Management System LLD

## Requirements
- Search for books by Author, Title, Genre
- Check if book is available
- Check out the book on a library card
- Create a library card
- See what books I have rented

## Questions
- Are there multiple copies of a book? One copy of a book
- Are there checkout fees/late fees? No checkout fees, but there are late fees

## Objects

### Book
- Author
- Title
- Genre


### LibrarySystem
- Books[]
- Checkouts[]
- SearchBooks(author, genre, title)
- IsAvailable(book)
- CheckoutBook(book, member)


Singleton Pattern


### Members
- Name
- Email
- Phone


### Checkouts
- Book
- Member
- CheckoutDate
- ReturnDate
- CalculateFee()


## Flow Diagram

1. User signs up
2. Member searches for book
3. Member checks if its available
4. If it is available, member checks it out
5. Member returns book
6. System Calculates fees if any


