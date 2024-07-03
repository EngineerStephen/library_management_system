


class Book_Operations:
    books = []
    def __init__(self, title, author, bio, genre, pub_date, availability):
        self.__title = title
        self.__author = author
        self.__bio    = bio
        self.__genre = genre
        self.__pub_date = pub_date
        self.__is_available = True

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

    # method for borrowing a book
    def borrow_book(self):
        # if its available then we set use the setter to set it to the opposite which is False
        if self.get_availability():
            self.set_availability()
            return True #returns True that we are able to borrow the book
        return False


    def return_book(self):
        self.set_availability() #sets the availability back to true if its Fals
        
        

    def add_new_book(library): #this is not a method of the class as above, this is a function that takes in a library object as an argument
        while True:
            ask_for_book = input("Would you like to add a new book? (yes/no): ")
            if ask_for_book == "yes":
                title = input("Please enter the title of the book you would like to add: ")
                author = input("Please enter the author of the book you would like to add: ")
                bio = input("Please enter the biography of the bio of the book you would like to add: ")
                genre = input("Please enter the genre of the book you would like to add: ")
                pub_date = input("Please enter the publication date of the book you would like to add: ")

                book_detail = Book_Operations(title, author, bio, genre, pub_date)
                library[title] = book_detail

                
                print(f"{title} by {author} a {genre} published on {pub_date} has been added to the library.  ")
                
                
            elif ask_for_book == "no":

                print("Thank you for using the Library's Book Management System. Goodbye!")
                return
            else:
                print("Invalid input. Please enter yes or no")
                continue
            break
        
        return self.books

    def borrow_book(self):
        print("Please note that all entered book titles are case sensitive")
        while True:
            ask_for_borrow = input("Would you like to borrow a book? (yes/no): ")
            if ask_for_borrow == "yes":
                book_to_borrow = input("Please enter the title of the book you would like to borrow: ")
                if book_to_borrow in self.books:
                    print(f"{book_to_borrow} has been borrowed from the library")
                else:
                    print(f"{book_to_borrow} is not available in the library")
                    continue
            elif ask_for_borrow == "no":
                print("Thank you for using the Library's Book Management System. Goodbye!")
                return
            else:
                print("Invalid input. Please enter yes or no")
                continue
            break
        return self.books

    def return_book(self):
        print("Please note that all entered book titles are case sensitive")
        while True:
            ask_for_return = input("Would you like to return a book? (yes/no): ")
            if ask_for_return == "yes":
                book_to_return = input("Please enter the title of the book you would like to return: ")
                if book_to_return not in self.books:
                    print(f"{book_to_return} has been returned to the library")
                else:
                    print(f"{book_to_return} is not available in the library")
            elif ask_for_return == "no": 
                print("Thank you for using the Library's Book Management System. Goodbye!")
                return   
            
            else:
                print("Invalid input. Please enter yes or no")
                continue
            break
        return self.books
    
    def search_book(self):
        print("Please note that all entered book titles are case sensitive")
        while True:
            ask_to_search = input("What book would you like to search for? ") 
            if ask_to_search in self.books:
                print(f"{ask_to_search} has been found in the library,")
            else:
                print(f"{ask_to_search} is not available in the library")
            break
        return self.books
    
    def display_books(self): 
        for key,value in self.books:
            print(key, value) 
            
            
            
def main():
    
    user_interaction = UserInteraction() #creating an instance of the UserInteraction class
    user_interaction.display_menu() #calling the display_menu method from the UserInteraction class
    print()
    
    
    while True:  
        user_menu_choice = input("Please enter the number associated with your desired option: ") #getting user input for the menu choice

        #book operations
        if user_menu_choice == "1":
            user_interaction.display_book_operations()
            print()
            
            user_book_operation_choice = input("What do you want to do here: ") #getting user input for the book operation choice
            book = Book_Operations(author, bio, genre, pub_date, availability) #creating an instance of the Book class
            if user_book_operation_choice == "1":
                book.add_new_book(library)
            
            elif user_book_operation_choice == "2":
                book.borrow_book()
                
            elif user_book_operation_choice == "3":
                book.return_book()
            
            elif user_book_operation_choice == "4":
                book.search_book()
            
            else:
                print("You have not made a valid selection, please try again.")
                continue
            print() 
        
        
        # #user_operations
        # elif user_menu_choice == "2":
            
        #     user_operation = User_Operations()  
        #     print()
        #     user_operation.display_user_operations()
        #     user_operation_choice = input("What do you want to do here: ") #getting user input for the user operation choice

        #     if user_operation_choice == "1":
        #         user_operation.add_new_user()
                
        #     elif user_operation_choice == "2":
        #         user_operation.view_user_details()
            
                
        #     elif user_operation_choice == "3":
        #         user_operation.all_users()

        #     else:
        #         print("You have not made a valid selection, please try again.")
        #         continue
        #     print() 

        # #author operations
        # elif user_menu_choice == "3":
        #     author_operation = Author_Operations()
            
        #     user_interaction.display_author_operations()
        #     user_author_choice = input("What do you want to do here: ")
            
        #     if user_author_choice == "1":
        #         author_operation.add_new_author()
                
        #     elif user_author_choice == "2":
        #         author_operation.view_author_details()
                
        #     elif user_author_choice == "3":
        #         author_operation.all_authors()

        #     else:
        #         print("You have not made a valid selection, please try again.")
        #         continue
        #     print() 
            
        
        # elif user_menu_choice == "4":
        #     print("Thank you for using the Library's Book Management System. Goodbye!")
        #     break
        
        # else:
        #     print("Invalid input. Please enter a number between 1 and 3 inclusive")
        #     continue
        # break 
    
     
    
main()  