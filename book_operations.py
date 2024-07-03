
class Book_Operations:
    
    def __init__(self, title, author, bio, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__bio    = bio
        self.__genre = genre
        self.__pub_date = pub_date
        self.__is_available = True

        self.books = []
        
    # Getter and Setters
    def get_title(self):
        return self.__title

    # getter for __is_available
    def get_availability(self):
        return self.__is_available

    # setter for availability
    def set_availability(self):
        # if self.__is_available is True we set it to false
        if self.get_availability():
            self.__is_available = False
        # else self.__is_available is False we set it to true
        else:
            self.__is_available = True

    # getter for genre
    def get_genre(self):
        return self.__genre

    
    
    
    def add_new_book(library):
        while True:
            title = input("Please enter the title of the book you would like to add: ")
            author = input("Please enter the author of the book you would like to add: ")
            bio = input("Please enter the biography of the bio of the book you would like to add: ")
            genre = input("Please enter the genre of the book you would like to add: ")
            pub_date = input("Please enter the publication date of the book you would like to add: ")

            book_detail = Book_Operations(title, author, bio, genre, pub_date)
            library[title] = book_detail
            print()
            print(f"{title} by {author} in {genre} genre published {pub_date} has been added to the library.  ")
            print()
            add_more = input("Would you like to add another book? (yes/no): ")
            if add_more.lower() == "yes":
                continue
            elif add_more.lower() == "no":
                print()
                print("Thank you for using the Library's Book Management System. Here are your books: ")
                
                if library == {}:
                    print("There are no books in the library")
                else:
                    for key, value in library:
                        print(key, value) 
                break
            else:
                print("Invalid input. Please enter yes or no")
                continue
            


    # method for borrowing a book
    def borrow_book(self):
        # if its available then we set use the setter to set it to the opposite which is False
        if self.get_availability():
            self.set_availability()
            return True #returns True that we are able to borrow the book
        return False


    def return_book(self):
        self.set_availability() #sets the availability back to true if its False
        
    
    def borrow_book(library):
        title = input("Please enter the title of the book you would like to borrow: ")
        if title in library:
            if title in library and library[title].borrow_book():#using the borrowed book method we created on this func 
                print(f"{title} has been borrowed")
                borrowed_books[title] = library[title]  
            else:
                print(f"Sorry, {title} is currently not available")
        else:
            print(f"{title} is not available in our library")

    def return_book(library):
        while True:
            try:
                title = input("Please enter the title of the book you would like to return: ")
                if library[title].get_availability():
                    print(f"{title} is already in the library. Please check the book title and try again")
                    continue
                elif library[title].get_availability() == False and title in borrowed_books:    
                        print("Thank you for returning the book")
                        library[title].return_book()
                        borrowed_books.pop(title)
                        break
                else:
                    print(f"{title} is not available in our library. Please check the book title and try again")
                    continue
            except KeyError:
                print(f"{title} is not available in our library. Please check the book title and try again")
            break

    
    def search_book(library):
        while True:
            title = input("Please enter the title of the book you would like to search: ")
            library
            if title in library:
                book = library[title]
                print("Book found, here is some info: ")
                print(book.get__title())
                print(book.get__author())
                print(book.get__genre())
                print(book.get__bio())
                print(book.get__pub_date())
                print(book.get__availability())     
            else:
                print(f"{title} is not available in the library")
            break
    
    # def display_books(library):
    #     for book in library.values():
    #     print(f"{book.get_title()} by {book.get_author()}: {book.get_genre()}: {book.get_availability()}")