# Book class
class Book:
    def __init__(self, name, author, release_date, read = False):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read = read

# Book collection class
class BookCollection:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError("List must contain only Book instances")
                
    def add_book(self, book):
        if isinstance(book,Book):
            self.books.append(book)
        else:
            raise Exception
        
    def mark_as_read(self, book_name):
        for book in self.books:
            if book_name == book:
                self.read = True
            else:
                print ("book not found in collection")

    def list_books(self):
        for book in self.books:
            print(book)

#Test your Code