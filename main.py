from user_interaction import UserInteraction    #importing the UserInteraction class from the user_interaction module
from book_operations import Book_Operations    #importing the Book class from the book_class module
from user_operations import User_Operations    #importing the User_Operations class from the user_operations module
from author_operations import Author_Operations   #importing the Author_Operations class from the author_operations module


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
            book = Book_Operations() #creating an instance of the Book class
            if user_book_operation_choice == "1":
                book.add_new_book()
            
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
        
        
        #user_operations
        elif user_menu_choice == "2":
            
            user_operation = User_Operations()  
            print()
            user_operation.display_user_operations()
            user_operation_choice = input("What do you want to do here: ") #getting user input for the user operation choice

            if user_operation_choice == "1":
                user_operation.add_new_user()
                
            elif user_operation_choice == "2":
                user_operation.view_user_details()
            
                
            elif user_operation_choice == "3":
                user_operation.all_users()

            else:
                print("You have not made a valid selection, please try again.")
                continue
            print() 

        #author operations
        elif user_menu_choice == "3":
            author_operation = Author_Operations()
            
            user_interaction.display_author_operations()
            user_author_choice = input("What do you want to do here: ")
            
            if user_author_choice == "1":
                author_operation.add_new_author()
                
            elif user_author_choice == "2":
                author_operation.view_author_details()
                
            elif user_author_choice == "3":
                author_operation.all_authors()

            else:
                print("You have not made a valid selection, please try again.")
                continue
            print() 
            
        
        elif user_menu_choice == "4":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            break
        
        else:
            print("Invalid input. Please enter a number between 1 and 3 inclusive")
            continue
        break 
    
    
    
    
    
    
    
main()  