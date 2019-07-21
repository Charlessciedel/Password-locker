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

    def test_init(self):
        """
        Test for correct initialization
        """
        self.assertEqual(self.new_user.first_name,"Charles")
        self.assertEqual(self.new_user.last_name,"Schiedel")
        self.assertEqual(self.new_user.password,"trewq")
    