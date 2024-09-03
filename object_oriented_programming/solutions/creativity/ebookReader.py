# Suppose you are on the design team for a new e-book reader.
# What are the primary classes and methods that the Python software for your reader will need?
# You should include an inheritance diagram for this code, but you do not need to write any actual code.
# Your software architecture should at least include ways for customers to buy new books,
# view their list of purchased books, and read their purchased books.


class Book:
    def __init__(self, id, details, title):
        self._id = id
        self._details = details
        self._title = title

class EBookReader:
    def __init__(self):
        self._books = {}
        self._purchased_books = {}

    def buy_new_books(self):
        if id in self._books:
            self._purchased_books.update(self._books[id])
        return "The requested book is not in available"

    # TODO: All purchased books should be added in the _purchased_books dict.

    def view_list_purchased_books(self):
        for key, value in self._purchased_books.items():
            return f"{self._purchased_books[key]['title']}: {self._purchased_books[key]['details']}"

    def read_purchased_books(self):
        pass

class Customer(EBookReader):
    def __init__(self, user, password):
        super().__init__()
        self._user = user
        self._password = password

