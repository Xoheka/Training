from datetime import datetime


class Author:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


class Book:
    def __init__(self, title, kind, authors, description, summary, rating):
        self.title = title
        self.kind = kind
        self.authors = authors
        self.description = description
        self.summary = summary
        self.rating = rating


bonifacy = Author('Bonifacy', 'Smith', datetime(1910, 10, 10))
john = Author('John', 'Smith', datetime(1905, 5, 15))
book = Book(
    "Przykładowy tytuł",
    'Kryminał',
)

