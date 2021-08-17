#### Application to store quotes from books I read.
#### 1- Get book name as argument value from command line.
#### 2- Check if book is in database (text file).
#### 3- If book is in database, ask user to enter quote.
#### 4-    save quote with book id.
#### 5- If book not in database, add that book.
#### 6-    ask user to enter quote.
#### 7-    save quote with book id.

import time

# BaseClass to hold global variable that will be used across other classes
class BaseClass:
    BOOKS_FILE   = 'books.dat'
    QUOTES_FILE  = 'quotes.dat'

class Book(BaseClass):
    
    #num_of_books = 0
    
    def __init__(self, book_id, book_title, book_auth=""):
        self.book_id = book_id
        self.book_title = book_title
        self.book_auth = book_auth
        self.quotes = []
        # load all quotes of this book instance by using the method "load_quotes"
        self.load_quotes(self.book_id)
        
        
        
        
    def __eq__(self, other):
        return (self.book_title, ) == (other.book_title, )
         
    def __hash__(self):
        return hash((self.book_title,))
         
#     def __str__(self):
#         return self.book_title
    
    def load_quotes(self, book_id):
        with open(BaseClass.QUOTES_FILE, "r") as f:
            all_quotes = f.readlines()
        
        for quote in all_quotes:
            current_quote = quote.split(',')
            #print(current_quote[1], book_id, current_quote[1] == book_id)
            if int(current_quote[1]) == int(book_id):
                self.quotes.append(current_quote[2])
        #print(all_quotes)
        
    def add_quote(self, quote):
        self.quotes.append(quote)
        
        
    def save_book(self):
        theBook = str(self.book_id) + ',' + self.book_title + ',' + self.book_auth + '\n'
        with open(BaseClass.BOOKS_FILE, 'a+') as f:
            f.write(theBook)
        
    def save_quotes(self):
        with open(BaseClass.QUOTES_FILE, 'a+') as f:
            for quote in self.quotes:
                f.write(quote + '\n')
                print(f'QUOTE {(quote)} SAVED!')
            
        
        
    def display_quotes(self):
        print('Book Title: ', self.book_title)
        print('Book Author: ', self.book_auth)
        print('Quotes:')
        if len(self.quotes) == 0:
            print('No quotes recoreded for this book.'.upper())
        else:
            for i, quote in enumerate(self.quotes):
                print('\t', i+1, quote)


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
        


class Books(BaseClass):
    
    def __init__(self):
        self.books_list = []
        self.quotes_list = []
        # Load books and quotes to fill books list and quotes list.
        self.load_books()
        self.load_all_quotes()
    
    # **************  Books methods  ******************
    
    def load_books_csv(self, file):
        pass
    
    def get_last_book_id(self):
        return int(self.books_list[-1].book_id)
    
    def add_book(self, new_book):  # new book passed as dictionary
        # create a new book instance
        newBook = Book(new_book['book_id'], new_book['book_title'], new_book['book_auth'])
        newBook.save_book()
        # Add new book to books list
        self.add_book_to_list(newBook)
        
    def load_books(self):
        with open(BaseClass.BOOKS_FILE, "r") as f:
            books = f.readlines()
        
        for book in books:
            current_book = book.split(",")
            print(current_book[0], current_book[1], current_book[2].strip("\n"))
            newBook = Book(current_book[0], current_book[1], current_book[2].strip("\n"))
            self.add_book_to_list(newBook)
            #newBook.load_quotes('quotes.dat', current_book[0])
            
    def get_num_of_books(self):
        return len(self.books_list)
    
    def get_book_by_index(self, index):
        return self.books_list[index]
    
        
    def add_book_to_list(self, book):
        #unique_books = set(self.books_list)
        #if book.book_title in unique_books:
        if book in self.books_list:
            print(f"Sorry, {book.book_title} already in list!")
        else:
            self.books_list.append(book)
    
    def delete_book_by_index(self, index):
        self.books_list.pop(index)
    
    def all_books(self):
        for item in self.books_list:
            print(item)
   
    def show_book_by_index(self, index):
        print(self.books_list[index].book_title)

    def display_books_list(self):
        #unique_books = set(self.books_list)
        for index, item in enumerate(self.books_list):
            print(index, item.book_id, item.book_title, item.book_auth)
  
   

    def save_books(self):
        with open(BaseClass.BOOKS_FILE, "w") as f:
            for book in self.books_list:
                f.write(str(book.book_id) + "," + book.book_title + "," + book.book_auth + "\n")
                #print("Saving " + str(book.book_id) + "," + book.book_title+"," + book.book_auth)
               
                
                
    def save_quotes(self):
        with open(BaseClass.QUOTES_FILE, "w") as f:
            for quote in self.quotes_list:
                f.write(str(quote.quote_id) + "," + quote.book_id + "," + quote.quote + "," + quote.page_number + "," + quote.volume_number + "\n")
                #print("Saving " + str(quote.quote_id) + "," + quote.book_id + "," + quote.quote + "," + quote.page_number + "," + quote.volume_number)
               
                
                
    

    # **************  Quotes methods  ******************

    def load_all_quotes(self):
        with open(BaseClass.QUOTES_FILE, 'r') as f:
            quotes = f.readlines()

        for quote in quotes:
            current_quote = quote.split(",")
            newQuote = Quote(current_quote[0], current_quote[1], current_quote[2], current_quote[3], current_quote[4].strip('\n'))
            self.add_quote_to_list(newQuote)
            
            
    def add_quote_to_list(self, quote):
        if quote in self.quotes_list:
            print(f"Sorry, {quote.quote} already in list!")
        else:
            self.quotes_list.append(quote)
            
    def display_quotes_list(self):
        for quote in self.quotes_list:
            print(quote.quote)
            
            
    def search_book_by_id(self, book_id):
        for item in self.books_list:
            if int(item.book_id) == int(book_id):
                #print("I found this book: ", item.book_title)
                return item
        
        return False
    
    
    def find_book_by_id(self, book_id):
        for index, item in enumerate(self.books_list):
            if int(item.book_id) == int(book_id):
                #print("I found this book: ", item.book_title)
                return index

        return -1
    
    
    def display_book_quotes(self, book_id):
        #current_book_id = self.search_book_by_id(book_id)
        this_book = self.search_book_by_id(book_id)
#         if this_book == False:
#             print("Sorry, this book is not in the DATABASE!")
#         else:
        this_book.display_quotes()
            


# App class implementation

class App():
    
    def __init__(self):
        # initialize main class 'Books'
        self.All_Books = Books()  
        
    def apply_changes(self):
        print()
        apply = input('Apply changes to file? (y/n).')
        if apply.upper() == 'Y':
            print('Applying Changes ... please, wait!')
            self.All_Books.save_books()
            time.sleep(2)
            print('Done.')
        
    def books_menu(self):
        while True:
            print('********************** Main Menu ************************')
            print()
            print(''.ljust(20), '1- Add Book.')
            print(''.ljust(20), '2- Update Book.')
            print(''.ljust(20), '3- Delete Book.')
            print(''.ljust(20), '4- Back.')
            print()
            choice = int(input('Please enter your choice:'))
            if choice == 1:
                new_book = {}
                print('************* Add New Book ************')
                print()
                # generate a new book id
                new_book['book_id'] = self.All_Books.get_last_book_id() + 1
                print('Book ID: ', new_book['book_id'])
                new_book['book_title'] = input('Enter book title: ')
                new_book['book_auth']  = input('Enter book Author')
                self.All_Books.add_book(new_book)
                self.apply_changes()
            if choice == 2:

                self.All_Books.display_books_list()
                book_id = input('Enter book ID (q to return): ')
                if book_id.upper() == 'Q':
                    pass
                else:
                    # convert book_id from str to int
                    book_id = int(book_id)
                    #update_book['book_id'] = book_id
                    book_index = self.All_Books.find_book_by_id(book_id)
                    if book_index < 0:
                        print('Sorry, book is not available!')
                    else:
                        update_book = self.All_Books.get_book_by_index(book_index)
                        print('Book ID:'.ljust(10), update_book.book_id)
                        print('(Enter nothing to keep field unchanged.)')
                        # get book title and validate it.
                        book_title = input(f'Book Title "{update_book.book_title}": ')
                        if book_title != update_book.book_title: # changed
                            if book_title != '':
                                update_book.book_title = book_title

                        # get book author and validate it.
                        book_auth  = input(f'Book Author "{update_book.book_auth}": ')
                        if book_auth != update_book.book_auth: # changed
                            if book_auth == '':
                                apply = input('WARNNING!, empty entry for author, apply anyway (y/n)?')
                                if apply.upper() == 'Y':
                                    update_book.book_auth = book_auth
                            else:
                                update_book.book_auth = book_auth

                        print('*********************************')
                        print(f'Book ID: {update_book.book_id}')
                        print(f'Book Title: {update_book.book_title}')
                        print(f'Book Author: {update_book.book_auth}')
                        print('*********************************')
                        self.apply_changes()
                        




            if choice == 3: # delete book
                self.All_Books.display_books_list()
                book_id = input('Enter book ID (q to return): ')
                if book_id.upper() == 'Q':
                    pass
                else:
                    # convert book_id from str to int
                    book_id = int(book_id)
                    #update_book['book_id'] = book_id
                    book_index = self.All_Books.find_book_by_id(book_id)
                    if book_index < 0:
                        print('Sorry, book is not available!')
                    else:
                        ask = input('Are you sure? (Y/n): ')
                        if ask.upper() == 'Y':
                            self.All_Books.delete_book_by_index(book_index)
                            self.apply_changes()
                        else:
                            print('Good thing.')
                        
            if choice == 4:
                break
            
            
    def main_menu(self):


        # Menu main loop

        while True:
            print('********************** Main Menu ************************')
            print()
            print(''.ljust(20), '1- Books.')
            print(''.ljust(20), '2- Load Quotes.')
            print(''.ljust(20), '3- Display Books.')
            print(''.ljust(20), '4- Display Quotes.')
            print(''.ljust(20), '5- Display A book Quotes.')
            print(''.ljust(20), '6- How many books?.')
            print(''.ljust(20), '7- Save Books and Quotes.')
            print(''.ljust(20), '8- Exit.')
            print()
            choice = int(input('Please enter your choice:'))
            if choice == 1:
                self.books_menu()
                #All_Books.load_books("books.dat")
            if choice == 2:
                self.All_Books.load_all_quotes()
            if choice == 3:
                self.All_Books.load_books()
                self.All_Books.display_books_list()
            if choice == 4:
                self.All_Books.display_quotes_list()
            if choice == 5:
                self.All_Books.display_books_list()
                book_id = input("Please, Enter book id: ")
                if len(book_id) == 0:
                    print("No book id provided!")
                else:
                    self.All_Books.display_book_quotes(book_id)
            if choice == 6:
                print('Number of books: >>>>', self.All_Books.get_num_of_books())
            if choice == 7:
                    print('Saving Books ....')
                    self.All_Books.save_books()
                    time.sleep(2)
                    print('Done.')
                    print('Saving Quotes ....')
                    self.All_Books.save_quotes()
                    time.sleep(2)
                    print('Done.')
            if choice == 8:
                print("Bye!")
                break
            #print('*********************************************************')

    def main(self):
        # Display menu
        self.main_menu()






myApp = App()
#print(myApp.num_books())
myApp.main()

