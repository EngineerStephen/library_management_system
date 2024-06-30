# class Books: 
#     def __init__(self, title, author, genre, pub_date, availability):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.pub_date = pub_date  
#         self.availability = availability
        
#         #initializing the list of books
#         self.books = []
        
#     #getter for title   
#     def get_title(self):
#         return self.title()
    
#     #getter for author   
#     def get_author(self):
#         return self.author()     
        
#     #getter for genre  
#     def get_genre(self):
#         return self.genre() 
        
#             #getter for title   
#     def get_availability(self):
#         return self.availability()
        
    
#     #function to add a new book       
#     def add_new_book(self,title):
#         ask_for_book = input("Would you like to add a new book? (yes/no): ")
#         if ask_for_book != "yes":
#             print("Thank you for using the Library's Book Management System. Goodbye!")
#             return         
#         else: 
#             new_book_title = input("Please enter the title of the book you would like to add: ")
#             self.books = self.books.append(new_book_title)
#             print(f"{new_book_title} has been added to the library")
            
            
            
#     #function to borrow a book
#     def borrow_book(self, title):
#         ask_for_borrow = input("Would you like to borrow a book? (yes/no): ")
#         if ask_for_borrow != "yes":
#             print("Thank you for using the Library's Book Management System. Goodbye!")
#             return         
#         else: 
#             book_to_borrow = input("Please enter the title of the book you would like to borrow: ")
#             self.title = self.title.remove(book_to_borrow)
#             print(f"{book_to_borrow} has been borrowed from the library")
        
        
#     #function to return a book
#     def return_book(self, title):
#         ask_for_return = input("Would you like to return a book? (yes/no): ")
#         if ask_for_return != "yes":
#             print("Thank you for using the Library's Book Management System. Goodbye!")
#             return         
#         else: 
#             book_to_return = input("Please enter the title of the book you would like to return: ")
#             self.title = self.title.append(book_to_return)
#             print(f"{book_to_return} has been returned to the library") 
            
            
#     #function to search for a book
#     def search_book(self, title):
#         ask_to_search = input("What book would you like to search for? ") 
#         if ask_to_search in self.title:
#             print(f"{ask_to_search} is available in the library")

#         else:
#             print(f"{ask_to_search} is not available in the library")
            

#     #function to display list of all books 
#     def display_books(self, title): 
#         for item in zip(self.title, self.author, self.pub_date, self.availability): #zip function to combine all the lists into a tuple
#             print(item) 
            
class Books:
        def __init__(self):
            self.books = {}
            
        def add_new_book(self):
            while True:
                ask_for_book = input("Would you like to add a new book? (yes/no): ")
                if ask_for_book == "yes":
                    new_book_title = input("Please enter the title of the book you would like to add: ")
                    new_book_author = input("Please enter the author of the book you would like to add: ")
                    new_book_bio = input("Please enter the biography of the author of the book you would like to add: ")    
                    new_book_genre = input("Please enter the genre of the book you would like to add: ")    
                    new_book_pub_date = input("Please enter the publication date of the book you would like to add: ")
                    
                    book_detail = {
                        {"author": new_book_author},
                        {"biography": new_book_bio},
                        {"genre": new_book_genre},
                        {"publication date": new_book_pub_date}
                        }
                
                    
                    self.books.append(book_detail)
                    
                    print(f"{new_book_title} has been added to the library.  ")
                    
                    
                elif ask_for_book == "no": 
                    print("Thank you for using the Library's Book Management System. Goodbye!")
                    return   
                
                else:
                    print("Invalid input. Please enter yes or no")
                    continue
                break
            
            return self.books
        
        def borrow_book(self):
            print("Please note that all entered book titles are case sensitive")
            while True:
                ask_for_borrow = input("Would you like to borrow a book? (yes/no): ")
                if ask_for_borrow == "yes":
                    book_to_borrow = input("Please enter the title of the book you would like to borrow: ")
                    if book_to_borrow in self.books:
                        print(f"{book_to_borrow} has been borrowed from the library")
                    else:
                        print(f"{book_to_borrow} is not available in the library")
                        continue
                elif ask_for_borrow == "no": 
                    print("Thank you for using the Library's Book Management System. Goodbye!")
                    return   
                
                else:
                    print("Invalid input. Please enter yes or no")
                    continue
                break
            return self.books
        
        def return_book(self):
            print("Please note that all entered book titles are case sensitive")
            while True:
                ask_for_return = input("Would you like to return a book? (yes/no): ")
                if ask_for_return == "yes":
                    book_to_return = input("Please enter the title of the book you would like to return: ")
                    if book_to_return not in self.books:
                        print(f"{book_to_return} has been returned to the library")
                    else:
                        print(f"{book_to_return} is not available in the library")
                elif ask_for_return == "no": 
                    print("Thank you for using the Library's Book Management System. Goodbye!")
                    return   
                
                else:
                    print("Invalid input. Please enter yes or no")
                    continue
                break
            return self.books
        
        def search_book(self):
            print("Please note that all entered book titles are case sensitive")
            while True:
                ask_to_search = input("What book would you like to search for? ") 
                if ask_to_search in self.books:
                    print(f"{ask_to_search} has been found in the library,")
                else:
                    print(f"{ask_to_search} is not available in the library")
                break
            return self.books
        
        def display_books(self): 
            for key,value in self.books:
                print(key, value) 