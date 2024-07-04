from user_interaction import UserInteraction, display_menu, display_book_operations, display_user_operations, display_author_operations    #importing the UserInteraction class from the user_interaction module
from book import Book_Operations, add_new_book,borrowing_book, return_book, search_book   #importing the Book class from the book_class module
from user import User_Operations, add_new_user, view_user_details, all_users   #importing the User_Operations class from the user_operations module
from author import Author_Operations, display_author_operations, add_new_author, view_author_details, all_authors   #importing the Author_Operations class from the author_operations module


#initializing the dictionaries
library = {}
users ={}
authors ={}


def main():
    
    while True: 
        print()
        display_menu() #calling the display_menu method from the UserInteraction class
        print()
        user_menu_choice = input("Please enter the number associated with your desired option: ") #getting user input for the menu choice
        print()
        #book operations
        if user_menu_choice == "1":
            display_book_operations()
            print()    
            user_book_operation_choice = input("Welcome to Book Operations. Please make your choice: ") #getting user input for the book operation choice
            print()
           #creating an instance of the Book class
            if user_book_operation_choice == "1":
                add_new_book(library)
            elif user_book_operation_choice == "2":
                borrowing_book(library)               
            elif user_book_operation_choice == "3":
                return_book()           
            elif user_book_operation_choice == "4":
                search_book(library )         
            else:
                print("You have not made a valid selection, please try again.")
                continue


        #user_operations
        elif user_menu_choice == "2":
            print()
            display_user_operations()
            print()
            user_operation_choice = input("Welcome to User Operations. Please make your choice:") #getting user input for the user operation choice
            print()
            if user_operation_choice == "1":
               add_new_user(users)               
            elif user_operation_choice == "2":
                view_user_details(users)
            elif user_operation_choice == "3":
                all_users(users)
            else:
                print("You have not made a valid selection, please try again.")
                continue
        
        #author_operations
        elif user_menu_choice == "3":
            print()
            display_author_operations(authors)
            print()
            user_author_operation_choice = input("Welcome to Author Operations. Please make your choice: ") #getting user input for the author operation choice
            print()
            if user_author_operation_choice == "1":
                add_new_author(authors)
            elif user_author_operation_choice == "2":
                view_author_details(authors)
            elif user_author_operation_choice == "3":
                all_authors(authors)
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

