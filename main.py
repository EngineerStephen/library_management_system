from user_interaction import UserInteraction    #importing the UserInteraction class from the user_interaction module
from book_class import Books    #importing the Book class from the book_class module

def main():
    user_interaction = UserInteraction() #creating an instance of the UserInteraction class
    user_interaction.display_menu() #calling the display_menu method from the UserInteraction class
    print()
    
    while True:  
        user_menu_choice = input("Please enter the number associated with your desired option: ") #getting user input for the menu choice
        
        #calling the display_book_operations method from the UserInteraction class
        if user_menu_choice == "1":
            user_interaction.display_book_operations()
            print()
            user_book_operation_choice = input("What do you want to do here: ") #getting user input for the book operation choice
            book = Books()
            
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
            
            
            
            
            
            
        elif user_menu_choice == "2": 
            user_interaction.display_user_operations()
        
        elif user_menu_choice == "3":
            user_interaction.display_author_operations()
        
        elif user_menu_choice == "4":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            break
        
        else:
            print("Invalid input. Please enter a number between 1 and 3 inclusive")
            continue
        break 
    
main()  