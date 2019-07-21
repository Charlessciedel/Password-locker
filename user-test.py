import unittest
from password import User

class TestUser(unittest.TestCase):
    """
    Class for testing the behaviour of the user class
    """
    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_user = User("Charles","Schiedel","trewq")