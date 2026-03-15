# Features to Implement
# Add a Book – Store title, author, year, and genres.
# View All Books – Display every book in the library.
# Search Books by Title – Case-insensitive match.
# Show Statistics – Number of books, unique authors, genres count.
# Exit – Ask for confirmation before quitting.

book = {}
library = []
authors = set()
genres = set()
search_title = ""
def menuSystem():    
    user_input = ""
    while user_input != "quit":
        user_input = input("""              
               1. Add a Book\n
               2. View All Books\n
               3. Search Books by Title\n
               4. Show Statistics\n
               5. Exit\n
               Please input the number where you want to navigate: """)
        if user_input == "1":
            addBook(library,authors,genres)
        elif user_input == "2":
            viewBooks(library)
        elif user_input == "3":
            searchBooks(library, search_title)
        elif user_input == "4":
            showStatistics(library, authors, genres)
        elif user_input == "5":
            if confirmExit():
                break
        else:
            print("Please input a number between 1 and 5")

def addBook(library, authors, genres):
    book_title = input("Please input the title of the Book: ").title()
    book_author = input("Please input the author of the Book: ").title()
    book_year = input("Please input the year of which the book was published: ")
    book_genres = tuple(input("Please input the genres of the book: ").split(","))
    book = {"title" : book_title, "author" : book_author, "year":book_year, "book_genres":book_genres}
    library.append(book.copy())
    authors.add(book_author)
    genres.add(book_genres)

def viewBooks(library):
    for book in library:
        print(book)

def searchBooks(library, search_title):
    search_title = input("Input the title of your book please: ").title()
    for book in library:
        if book["title"] == search_title:
            print("Book was found")
            print(book)
        elif book["title"] not in search_title:
            print("No book found")

def showStatistics(library, authors, genres):
    number_of_books = len(library)
    print(number_of_books)
    print(authors)
    print(genres)
    #nested loop to count how many books per genre
    genre_count = {}
    for book in library:
        for genre in book["book_genres"]:
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
    print(genre_count)
        

def confirmExit():
    choice = input("Are you sure you want to exit? (y/n) ")
    if choice == "y":
        return True
    else:
        return False


menuSystem()