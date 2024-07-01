user_operation_menu = ["Add a new user", "View user details", " Display all users"]   
 
class User_Operations: 
    def __init__(self):
        # self.__user_name = user_name
        # self.__user_id = user_id 
        # self._borrowed_books = borrowed_books
        self.user = {}
        
    #Displaying the menu 
    def display_user_operations(self):
        numbered_operations = [(i + 1, item ) for i, item in enumerate(user_operation_menu)]
        for i, item in numbered_operations:
            print(i,item)
        return "Welcome to User Operations. Please make your choice:  "

        
    #function to add a new user
    def add_new_user(self):
        ask_for_user = input("Would you like to add a new user? (yes/no): ")
        if ask_for_user != "yes":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            return   
            
        else: 
            new_user_name = input("Please enter the name of the user you would like to add: ")
            new_user_id = input("Please enter the id of the user you would like to add: ")
            new_user_detail = {new_user_name: new_user_id}
            self.user.update(new_user_detail)
            print(f"{new_user_name} has been added to the library")
            print(new_user_detail)

    
    #viewing user's details
    def view_user_details(self):
        while True:
            ask_to_view = input("Would you like to view a user detail? (yes/no): ")
            if ask_to_view != "yes":
                print("Thank you for using the Library's Book Management System. Goodbye!")
                return   
            else:
                my_user_name = input("Please enter the name of the user you would like to view: ")
                
                if my_user_name in self.user:
                    print(f"{my_user_name} is available in the library")
                    for name, id in self.user.items(my_user_name):
                        print(name, id)
                        
                else:
                    print(f"{my_user_name} is not available in the library")
                    continue    
                
                
                
            
    #function to view all user details
    def all_users(self):
        print("The following are the details of all the users in the library: ")
        for user, id in self.user: #zip function to combine all the lists into a tuple
            print(user, id) 
            
        if self.user == {}:
            print("There are no users in the library")
            return
            