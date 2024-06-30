
#the list of choices available to the user
main_menu = ["Book Operations", "User Operations", "Author Operations", "Quit"]
book_operations = ["Add a new book", "Borrow a book", "Return a book", "Search for a book"]
user_operations = ["Add a new user", "View user details", " Display all users"]
author_operations = ["Add a new author", "View author details", "Display all authors"]


#greeting the user and displaying the menu
def user_greet():
    print()
    from datetime import datetime
    today = datetime.today()
    print(f"Hello, Today is {today}. Welcome to the Library's Book Management System (LBMS).")
    user_name = input("Please tell me your name: ").capitalize()
    print(f"Nice to meet you {user_name},", end=" ")
    print(" What would you like to do in your favorite LBMS? Please choose from the list below:")
    

user_greet()



class UserInteraction:
    def __init__(self):
        pass

    #Displaying the menu 
    def display_menu(self):
        numbered_menu = [(i + 1, menu) for i, menu in enumerate(main_menu)]
        for i, menu in numbered_menu:
            print(i,menu)
        return "Please make your choice:  "    

    #Displaying the book operations menu
    def display_book_operations(self):
        numbered_book_operations = [(i + 1, menu) for i, menu in enumerate(book_operations)]
        for i, menu in numbered_book_operations:
            print(i,menu)
        return "Please make your choice:  "    

    #Displaying the user operations menu
    def display_user_operations(self):
        numbered_user_operations = [(i + 1, menu) for i, menu in enumerate(user_operations)]
        for i, menu in numbered_user_operations:
            print(i,menu)
        return "Please make your choice:  "    

    #Displaying the author operations menu
    def display_author_operations(self):
        numbered_author_operations = [(i + 1, menu) for i, menu in enumerate(author_operations)]
        for i, menu in numbered_author_operations:
            print(i,menu)
        return "Please make your choice:  "    

    #Displaying the book operations menu
    def display_book_operations(self):
        numbered_book_operations = [(i + 1, menu) for i, menu in enumerate(book_operations)]
        for i, menu in numbered_book_operations:
            print(i,menu)
        return "Welcome to Book operations. Please make your choice:  "    

    #Displaying the user operations menu
    def display_user_operations(self):
        numbered_user_operations = [(i + 1, menu) for i, menu in enumerate(user_operations)]
        for i, menu in numbered_user_operations:
            print(i,menu)
        return "Welcome to User Operations. Please make your choice:  "    

    #Displaying the author operations menu
    def display_author_operations(self):
        numbered_author_operations = [(i + 1, menu) for i, menu in enumerate(author_operations)]
        for i, menu in numbered_author_operations:
            print(i,menu)
        return "Welcome to Author Operations. Please make your choice:  "    

    #Displaying the book operations menu
    def display_book_operations(self):
        numbered_book_operations = [(i + 1, menu) for i, menu in enumerate(book_operations)]
        for i, menu in numbered_book_operations:
            print(i,menu)
        return "Welcome to Book Operations. Please make your choice:  "   

    