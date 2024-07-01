
author_operation_menu = ["Add a new author", "View author details", "Display all authors"]



class Author_Operations: 
    def __init__(self):
        self.author = {}

    #Displaying the menu
    def display_author_operations(self):
        numbered_author_operations = [(i + 1, item ) for i, item in enumerate(author_operation_menu)]
        for i, item in numbered_author_operations:
            print(i,item)
        return "Welcome to Author Operations. Please make your choice:  "
    
    
    def add_new_author(self):

        ask_for_author = input("Would you like to add a new author? (yes/no): ")
        if ask_for_author!= "yes":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            return   
            
        else: 
            new_author = input("Please enter the name of the author you would like to add: ")
            new_author_biography = input("Please enter the biography of the author you would like to add: ")
            new_author_detail = {new_author: new_author_biography}
            self.author.update(new_author_detail)
            print(f"{new_author} has been added to the library")
            print(new_author_detail)
            
            
     #function to view specific author's details       
    def view_author_details(self):
        while True:
            ask_to_view = input("Would you like to view an author detail? (yes/no): ")
            if ask_to_view != "yes":
                print("Thank you for using the Library's Book Management System. Goodbye!")
                return   
            else:
                my_author_name = input("Please enter the name of the author you would like to view: ")
                
                if my_author_name in self.author:
                    print(f"{my_author_name} is available in the library")
                    for name, bio in self.author.items(my_author_name):
                        print(name, bio)
                        
                else:
                    print(f"{my_author_name} is not available in the library")
                    continue

    #function to view all author details
    def all_authors(self):
        if self.author == {}:
            print("There are no authors in the library")

        else:
            print("The following are the details of all the authors in the library: ") 
            for author, bio in self.author.items():
                print(author, bio)
            