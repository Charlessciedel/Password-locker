import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):
    """
    Class to test behaviour of the credentials class
    """
    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_credentials = Credentials("LMS","Charlie","kanambo")

    def tearDown(self):
        """
        Method that cleans up after each test
        """
        Credentials.credentials_list = []

    def test_init(self):
        """
        Test for correct initialization
        """
        self.assertEqual(self.new_credentials.account_name,"LMS")
        self.assertEqual(self.new_credentials.username,"Charlie")
        self.assertEqual(self.new_credentials.password,"Kanambo")
