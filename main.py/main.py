from book import Book
from library import Library

def main():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)
    library.list_books()

if __name__ == "__main__":
    main()

