user_operation_menu = ["Add a new user", "View user details", " Display all users"]   

class User_Operations: 
    def __init__(self, user_name, user_id, borrowed_books):
        self.__user_name = user_name
        self.__user_id = user_id 
        self.__borrowed_books = borrowed_books
    
        self.users={}
    
    #getter for user_name  
    def get_user_name(self):
        return self.__user_name
    
    #getter for user_id
    def get_user_id(self):
        return self.__user_id
    
    #getter for borrowed_books  
    def get_borrowed_books(self):
        return self.__borrowed_books    
    
    #setter for user_name   
    def set_user_name(self, user_name):
        self.__user_name = user_name

    #setter for user_id
    def set_user_id(self, user_id): 
        self.__user_id = user_id    
        
    #setter for borrowed_books
    def set_borrowed_books(self, borrowed_books):
        self.__borrowed_books = borrowed_books  

    
        
    #Displaying the menu 
    def display_user_operations(users):
        numbered_operations = [(i + 1, item ) for i, item in enumerate(user_operation_menu)]
        for i, item in numbered_operations:
            print(i,item)
        return "Welcome to User Operations. Please make your choice:  "

        
    #function to add a new user

    def add_new_user(users): 
    
        new_user_name = input("Please enter the name of the user you would like to add: ")
        new_user_id = input("Please enter the id of the user you would like to add: ")
        new_user_borrowed = input("Please enter the borrowed books of the user you would like to add: ")    
        
        user_detail = User_Operations(new_user_name, new_user_id, new_user_borrowed)
        users.update({new_user_name: user_detail}) 
        print(f"User: {new_user_name} with ID: {new_user_id} has been added to the library")

    #viewing user's details
    def view_user_details(users):
        
            user_search = input("Please, enter the name of the user you would like to view: ")
            if user_search in users:
                print(f"{user_search} is available in the library")
                specified_user = users[user_search]
                print(f"User Name: {specified_user.get_user_name()}")
                print(f"User ID: {specified_user.get_user_id()}")
                print(f"Borrowed Books: {specified_user.get_borrowed_books()}")
            else:
                print(f"{user_search} is not available in the library")
            

            

            
    #function to view all user details
    def all_users(users):
        if not users:  # Check if users dictionary is empty
            print("There are no users in the library")
        else:
            print("The following are the details of all the users in the library: ")
            # user_detail = users
            for user_name, user_detail in users.items():
                print(f"User Name: {user_detail.get_user_name()}")
                print(f"User ID: {user_detail.get_user_id()}")
                print(f"Borrowed Books: {user_detail.get_borrowed_books()}")
                print()