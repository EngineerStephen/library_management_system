
author_operation_menu = ["Add a new author", "View author details", "Display all authors"]



class Author_Operations: 
    def __init__(self, author_name, author_bio, books):
        self.__author_name = author_name
        self.__author_bio = author_bio
        self.__books = books
        self.author = {}
        
        
    #getter for author_name 
    def get_author_name(self):
        return self.__author_name
    
    #getter for author_bio  
    def get_author_bio(self):
        return self.__author_bio
    
    #getter for books
    def get_books(self):
        return self.__books
    
    #setter for author_name
    def set_author_name(self, author_name):
        self.__author_name = author_name
        
    #setter for author_bio
    def set_author_bio(self, author_bio):
        self.__author_bio = author_bio
           

#Displaying the menu
def display_author_operations(self):
    numbered_author_operations = [(i + 1, item ) for i, item in enumerate(author_operation_menu)]
    for i, item in numbered_author_operations:
        print(i,item)
    return "Welcome to Author Operations. Please make your choice:  "


def add_new_author(authors):
    
    new_author_name = input("Please enter the name of the author you would like to add: ")      
    new_author_bio = input("Please enter the biography of the author you would like to add: ")
    new_author_books = input("Please enter the books of the author you would like to add: ")      
    
    author_detail = Author_Operations(new_author_name, new_author_bio, new_author_books)
    authors.update({new_author_name: author_detail})
    print(f"Author: {new_author_name}, has been added to the library")
    

#function to view specific author's details   
def view_author_details(authors):
    
    author_search = input("Please, enter the name of the author you would like to view: ")
    if author_search in authors:
        print(f"{author_search} is available in the library")   
        specified_author = authors[author_search]
        print(f"Author Name: {specified_author.get_author_name()}")
        print(f"Author Bio: {specified_author.get_author_bio()}")
        print(f"Author Books: {specified_author.get_books()}")
    else:
        print(f"{author_search} is not available in the library")


#function to view all author details
def all_authors(authors):
    if not authors:
        print("There are no authors in the library")

    else:
        print("The following are the details of all the authors in the library: ") 
        for author_name, author_detail in authors.items():
            print(f"Author Name: {author_detail.get_author_name()}")
            print(f"Author Bio: {author_detail.get_author_bio()}")
            print(f"Author Books: {author_detail.get_books()}")
            
            
            
        