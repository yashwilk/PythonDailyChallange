"""Simple Explanation of Your Library Management System"""
#small library in a school.
#📚 Books
#👦 Members (people who borrow books)
#🏢 Library
#A class is like a blueprint or a template.
"""Book → blueprint for books
Member → blueprint for members
Library → blueprint for the library"""


class Books:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isavailable = True

    def display_info(self):
        status = "Available" if self.isavailable else "Not Available"
        print(f"{self.title} by {self.author} - {status}")




class Members:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.isavailable:
            book.isavailable = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already issued")