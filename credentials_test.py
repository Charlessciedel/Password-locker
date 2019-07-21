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

    def test_save_credentials(self):
        """
        Test to check whether app saves account credentials
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        """
        Test for saving multiple credentials
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("AllFootball","Kibet","messithegoat")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)