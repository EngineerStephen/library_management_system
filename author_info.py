    
class Author: 
    def __init__(self, book_authors, author_biography):
        self.book_authors = book_authors
        self.author_biography = author_biography
        
    #I do not need getters for these because they are public attributes 
    
    def add_new_author(self):
        new_author_detail = {}
        ask_for_author = input("Would you like to add a new author? (yes/no): ")
        if ask_for_author!= "yes":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            return   
            
        else: 
            new_author = input("Please enter the name of the author you would like to add: ")
            self.book_authors = self.book_authors.append(new_author)
            new_author_biography = input("Please enter the biography of the author you would like to add: ")
            self.author_biography = self.author_biography.append(new_author_biography)
            new_author_detail = {new_author :  new_author_biography}
            print(f"{new_author} has been added to the library")
            print(new_author_detail)

    #function to view all user details
    def all_authors(self):
        details = self.book_authors, self.author_biography
        print("The following are the details of all the authors in the library: ")
        for detail in zip(self.book_authors, self.author_biography): #zip function to combine all the lists into a tuple
            print(detail) 