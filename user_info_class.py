    
class User: 
    def __init__(self, user_name, user_id, borrowed_books):
        self.__user_name = user_name
        self.__user_id = user_id 
        self._borrowed_books = borrowed_books
        
    #getter for user_name
    def get_user_name(self):
        return self._user_name

    #getter for id   
    def get_user_id(self):
        return self.__user_id 
    
    #getter for borrowed_books
    def get_borrowed_books(self):
        return self._borrowed_books 
    
    
    # setter for a new user
    def set_user_name(self, new_user_name):
        self.__user_name = new_user_name
    
    # setter for new_user_id
    def set_user_id(self, new_user_id):
        self.__user_id = new_user_id
        print(self.__user_id, )
        
        
    #function to add a new user
    def add_new_user(self):
        new_user_detail = {}
        ask_for_user = input("Would you like to add a new user? (yes/no): ")
        if ask_for_user != "yes":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            return   
            
        else: 
            new_user = input("Please enter the name of the user you would like to add: ")
            self.__user_name = self.__user_name.append(new_user)
            new_user_id = input("Please enter the id of the user you would like to add: ")
            self.__user_id = self.__user_id.append(new_user_id)
            new_user_detail = {new_user: new_user_id}
            print(f"{new_user} has been added to the library")
            print(new_user_detail)

    #function to view all user details
    def all_users(self):
        details = self.__user_name, self.__user_id
        print("The following are the details of all the users in the library: ")
        for detail in zip(self.__user_name, self.__user_id): #zip function to combine all the lists into a tuple
            print(detail) 