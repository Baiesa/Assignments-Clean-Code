'''
Task 1: Designing the Book Module

Create a module for managing book-related functionalities. This includes classes and functions for book attributes, 
book availability, and any other book-specific operations.

Problem Statement:

The bookstore system requires a dedicated module for handling various aspects related to books, such as title, author, 
price, and stock status.
'''
from book_manager import Book

my_book = Book("Python complecated", "Baies Aziz", 20000 , 2)

print("Book Details",my_book)

print("Check availability")
if my_book.check_availability():
    print("My book is available")
else:
    print("Sorry the legend is sleep now lol")

print("Borrow book")
my_book.borrow_book()

print("Returned book")
my_book.return_book()


