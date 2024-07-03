from user_interaction import UserInteraction    #importing the UserInteraction class from the user_interaction module
from book_operations import Book_Operations    #importing the Book class from the book_class module
from user_operations import User_Operations    #importing the User_Operations class from the user_operations module
from author_operations import Author_Operations   #importing the Author_Operations class from the author_operations module


#initializing the dictionaries
library = {}
borrowed_books = {}
users ={}
authors ={}


def main():
    
    while True:
        user_interaction = UserInteraction() 
        print()
        user_interaction.display_menu() #calling the display_menu method from the UserInteraction class
        print()
        user_menu_choice = input("Please enter the number associated with your desired option: ") #getting user input for the menu choice
        print()
        #book operations
        if user_menu_choice == "1":
            user_interaction.display_book_operations()
            print()    
            user_book_operation_choice = input("Welcome to Book Operations. Please make your choice: ") #getting user input for the book operation choice
            print()
           #creating an instance of the Book class
            if user_book_operation_choice == "1":
                Book_Operations.add_new_book(library)
            elif user_book_operation_choice == "2":
                Book_Operations.borrow_book(library)               
            elif user_book_operation_choice == "3":
                Book_Operations.return_book(library)           
            elif user_book_operation_choice == "4":
                Book_Operations.search_book(library )         
            else:
                print("You have not made a valid selection, please try again.")
                continue


        #user_operations
        elif user_menu_choice == "2":
            print()
            User_Operations.display_user_operations(users)
            print()
            user_operation_choice = input("Welcome to User Operations. Please make your choice:") #getting user input for the user operation choice
            print()
            if user_operation_choice == "1":
                User_Operations.add_new_user(users)               
            elif user_operation_choice == "2":
                User_Operations.view_user_details(users)
            elif user_operation_choice == "3":
                User_Operations.all_users(users)
            else:
                print("You have not made a valid selection, please try again.")
                continue
        
        #author_operations
        elif user_menu_choice == "3":
            print()
            Author_Operations.display_author_operations(authors)
            print()
            user_author_operation_choice = input("Welcome to Author Operations. Please make your choice: ") #getting user input for the author operation choice
            print()
            if user_author_operation_choice == "1":
                Author_Operations.add_new_author(authors)
            elif user_author_operation_choice == "2":
                Author_Operations.view_author_details(authors)
            elif user_author_operation_choice == "3":
                Author_Operations.all_authors(authors)
            else:
                print("You have not made a valid selection, please try again.")
                continue


        elif user_menu_choice == "4":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            break
        
        else:
            print("Invalid input. Please enter a number between 1 and 3 inclusive")
            continue


main()  

