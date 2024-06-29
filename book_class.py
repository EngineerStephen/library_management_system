class Books: 
    def __init__(self, title, author, genre, pub_date, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date = availability  
        self.availability = availability
    
    #getter for title   
    def get_title(self):
        return self.title()
    
    #getter for author   
    def get_author(self):
        return self.author()     
        
    #getter for genre  
    def get_genre(self):
        return self.genre() 
        
            #getter for title   
    def get_availability(self):
        return self.availability()
        
    
    #function to add a new book       
    def add_new_book(self,title):
        ask_for_book = input("Would you like to add a new book? (yes/no): ")
        if ask_for_book != "yes":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            return         
        else: 
            new_book = input("Please enter the title of the book you would like to add: ")
            self.title = self.title.append(new_book)
            print(f"{new_book} has been added to the library")
            
            
            
    #function to borrow a book
    def borrow_book(self, title):
        ask_for_borrow = input("Would you like to borrow a book? (yes/no): ")
        if ask_for_borrow != "yes":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            return         
        else: 
            book_to_borrow = input("Please enter the title of the book you would like to borrow: ")
            self.title = self.title.remove(book_to_borrow)
            print(f"{book_to_borrow} has been borrowed from the library")
        
        
    #function to return a book
    def return_book(self, title):
        ask_for_return = input("Would you like to return a book? (yes/no): ")
        if ask_for_return != "yes":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            return         
        else: 
            book_to_return = input("Please enter the title of the book you would like to return: ")
            self.title = self.title.append(book_to_return)
            print(f"{book_to_return} has been returned to the library") 
            
            
    #function to search for a book
    def search_book(self, title):
        ask_to_search = input("What book would you like to search for? ") 
        if ask_to_search in self.title:
            print(f"{ask_to_search} is available in the library")

        else:
            print(f"{ask_to_search} is not available in the library")
            

    #function to display list of all books 
    def display_books(self, title): 
        for item in zip(self.title, self.author, self.pub_date, self.availability): #zip function to combine all the lists into a tuple
            print(item) 
            
    