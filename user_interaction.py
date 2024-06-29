
#the list of choices available to the user
main_menu = ["Book Operations", "User Operations", "Author Operations", "Quit"]
book_operations = [" Add a new book", "Borrow a book", "Return a book", "Search for a book"]
user_operations = ["Add a new user", "View user details", " Display all users"]
author_operations = ["Add a new author", "View author details", "Display all authors"]

#greeting the user
print()
user_name = input("Hello, Welcome to the Library's Book Management System (LBMS). Please tell me your name: ").capitalize()
print()

from datetime import datetime
today = datetime.today()
print(user_name + ", Nice to meet you!", end=" ")
print(f"Today is {today}. Where would you like to go to in your favorite LBMS? Please choose from the list below: ")

#Displaying the menu 
def display_menu():
    numbered_menu = [(i + 1, menu) for i, menu in enumerate(main_menu)]
    for i, menu in numbered_menu:
        print(i,menu)
    return "Please make your choice:  "    

print(display_menu())
    