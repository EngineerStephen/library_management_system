def add_new_user():
        new_user_detail = {}
        ask_for_user = input("Would you like to add a new user? (yes/no): ")
        if ask_for_user != "yes":
            print("Thank you for using the Library's Book Management System. Goodbye!")
            return   
            
        else: 
            new_user = input("Please enter the name of the user you would like to add: ")
            self.user_name = self.user_name.append(new_user)
            new_user_id = input("Please enter the id of the user you would like to add: ")
            self.__user_id = self.__user_id.append(new_user_id)
            new_user_detail = {new_user: new_user_id}
            print(f"{new_user} has been added to the library")
            print(new_user_detail)
print(add_new_user())