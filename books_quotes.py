class Book:
    def __init__(self, book_id, book_title, book_auth=""):
        self.book_id = book_id
        self.book_title = book_title
        self.book_auth = book_auth
        self.quotes = []
        
        
    def __eq__(self, other):
        return (self.book_title, ) == (other.book_title, )
         
    def __hash__(self):
        return hash((self.book_title,))
         
    def __str__(self):
        return self.book_title
    
    
    def add_quote(self, quote):
        self.quotes.append(quote)
        
    def display_quotes(self):
        for quote in self.quotes:
            print(quote.quote)


class Quote():
    def __init__(self, quote_id, book_id, quote, page_number, volume_number=1):
        self.quote_id = quote_id
        self.book_id = book_id
        self.quote = quote
        self.page_number = page_number
        self.volume_number = volume_number
        
    def __eq__(self, other):
        return (self.quote, ) == (other.quote, )
         
    def __hash__(self):
        return hash((self.quote,))
         
    def __str__(self):
        return self.quote


class Books:
    def __init__(self):
        self.books_list = []
        self.quotes_list = []

    # **************  Books methods  ******************

    def load_books(self, file):
        with open(file, "r") as f:
            books = f.readlines()

        for book in books:
            current_book = book.split(",")
            #print(current_book[0], current_book[1], current_book[2].strip("\n"))
            newBook = Book(current_book[0], current_book[1], current_book[2].strip("\n"))
            self.add_book_to_list(newBook)


    def add_book_to_list(self, book):
        #unique_books = set(self.books_list)
        #if book.book_title in unique_books:
        if book in self.books_list:
            print(f"Sorry, {book.book_title} already in list!")
        else:
            self.books_list.append(book)


    def all_books(self):
        for item in self.books_list:
            print(item)


    def display_books_list(self):
        #unique_books = set(self.books_list)
        for item in self.books_list:
            print(item.book_id, item.book_title, item.book_auth)


    def search_book_by_id(self, book_id):
        for item in self.books_list:
            if item.book_id == book_id:
                print("I found this book: ", item.book_title)


    def save_books(self, file):
        with open(file, "w") as f:
            for book in self.books_list:
                f.write(str(book.book_id)+","+book.book_title+","+book.book_auth+"\n")



    # **************  Quotes methods  ******************

    def load_quotes(self, file):
        with open(file, 'r') as f:
            quotes = f.readlines()

        for quote in quotes:
            current_quote = quote.split(",")
            newQuote = Quote(current_quote[0], current_quote[1], current_quote[2], current_quote[3], current_quote[4])
            self.add_quote_to_list(newQuote)


    def add_quote_to_list(self, quote):
        if quote in self.quotes_list:
            print(f"Sorry, {quote.quote} already in list!")
        else:
            self.quotes_list.append(quote)

    def display_quotes_list(self):
        for quote in quotes_list:
            print(quote.quote)


def menu():
    # initiate main class
    All_Books = Books()
    while True:
        print('********************** Main Menu ************************')
        print()
        print(''.ljust(20), '1- Load Books.')
        print(''.ljust(20), '2- Load Quotes.')
        print(''.ljust(20), '3- Display Books.')
        print(''.ljust(20), '4- Display Quotes.')
        print(''.ljust(20), '5- Exit.')
        print()
        choice = int(input('Please enter your choice:'))
        if choice == 1:
            All_Books.load_books("books.dat")
        if choice == 2:
            All_Books.load_quotes("quotes.dat")
        if choice == 3:
            All_Books.display_books_list()
        if choice == 4:
            All_Books.display_quotes_list()
        if choice == 5:
            break
        #print('*********************************************************')


def main():
    # Display menu
    menu()


main()

