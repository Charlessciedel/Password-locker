import string
import random
class User:
    """
    Class to define login details for the user in the application
    """
    user_list = []

    def __init__(self,first_name,last_name,password):
        """
        Function to initialize user fields correctly
        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
                                        
    def save_user(self):
        """
        Function to save user login details
        """
        User.user_list.append(self)

        
class Credentials:
    """
    Class to define credentials for the different accounts
    """
    credentials_list = []

    def __init__(self,account_name,username,password):
        """
        Function th initialize credential fields correctly
        """

        self.account_name = account_name
        self.username = username
        self.password = password