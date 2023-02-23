from user import User

class Privilege:
    """This class models privilages of an admin"""

    def __init__(self, privilages=['can add post', 'can delete post', 'can ban user', 
            'Create User', 'Update User', 'Display User\'s information ', 'Delete User', ]
            ):
        self.privilages = privilages

    def show_privileges(self):
        print("List of Admin Privileges are:")
        for privilege in self.privilages:
            print(f" - {privilege}")
        return ""


class Admin(User):
    """This an Admin model that inherit from the User class""" 

    def __init__(self, first_name, last_name, *user_profile):
        super().__init__(first_name, last_name, *user_profile)
        self.privileges = Privilege()

    
