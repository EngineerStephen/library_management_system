borrowed_books = {}


class Book_Operations:
    
    def __init__(self, title, author, bio, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__bio    = bio
        self.__genre = genre
        self.__pub_date = pub_date
        self.__is_available = True


    # Getter and Setters
    def get_title(self):
        return self.__title
    
    # getter for author
    def get_author(self):
        return self.__author
    
    # getter for bio
    def get_bio(self):
        return self.__bio
    
    # getter for genre
    def get_genre(self):
        return self.__genre
    
    
    # getter for publication date
    def get_pub_date(self):
        return self.__pub_date
    

    # getter for __is_available
    def get_availability(self):
        return self.__is_available

    # method for borrowing a book
    def borrow_book(self):
        # if its available then we set use the setter to set it to the opposite which is False
        # if self.__is_available:
            self.__is_available = False
            # return True #returns True that we are able to borrow the book
        # else: #if its not available then we return False
        #     return False


    # method for returning a book   
    def return_book(self):
        self.__is_available = True
    

def add_new_book(library):
    
    title = input("Please enter the title of the book you would like to add: ")
    author = input("Please enter the author of the book you would like to add: ")
    bio = input("Please enter the biography of the bio of the book you would like to add: ")
    genre = input("Please enter the genre of the book you would like to add: ")
    pub_date = input("Please enter the publication date of the book you would like to add: ")
    
    book_details  = Book_Operations(title, author, bio, genre, pub_date)
    library[title] = book_details
    # library.update({title: book_details})
    print(f"Book: {title} by {author} has been added to the library")


def borrowing_book(library):
    title = input("Please enter the title of the book you would like to borrow: ")
    if title in library:
        if library[title].get_availability() == True:
            library[title].borrow_book()#using the borrowed book method we created on this func 
            borrowed_books[title] = library[title]
            print(f"You have successfully borrowed {title} from the library")  
        
        else:
            print(f"{title} is not available for borrowing at the moment. Please try again later.")

    else:
        print(f"{title} is not available in our library")

def return_book():
    while True:
            title = input("Please enter the title of the book you would like to return: ")
            if title in borrowed_books:
                borrowed_books[title].return_book()
                borrowed_books.pop(title)
                print(f"Thank you for returning {title} to the library.")
                break
            else:
                print(f"{title} is not available in our library. Please check the book title and try again")


def search_book(library):
        title = input("Please enter the title of the book you would like to search: ")
        if title in library:
            book = library[title]
            print("Book found, here is some info: ")
            print(f"Title: {book.get_title()}")
            print(f"Author: {book.get_author()}")
            print(f"Genre: {book.get_genre()}")
            print(f"Author's Bio: {book.get_bio()}")
            print(f"Pub_date: {book.get_pub_date()}")
            print(f"Available? True/False: {book.get_availability()}")     
        else:
            print(f"{title} is not available in the library")


# def display_books(library):
#     for book in library.values():
#     print(f"{book.get_title()} by {book.get_author()}: {book.get_genre()}: {book.get_availability()}")