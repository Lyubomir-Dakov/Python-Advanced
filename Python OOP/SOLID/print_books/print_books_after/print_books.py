class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book):
        return book.content


class Printer:
    def get_book(self, book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book