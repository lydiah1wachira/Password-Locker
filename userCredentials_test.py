import unittest
from users import User
from credentials import Credentials

class TestClass(unittest.TestCase):
  '''
  Test class that defines test cases for the User class behaviours.
  '''
  def setUp(self):
    '''
    set up method to run before each individual test case
    '''
    self.new_user = User('Severus Snape', 'Expelliarmus')

  def test_init(self):
    '''
    test case to check if object is being initialized correctly
    '''
    self.assertEqual(self.new_user.username,'Severus Snape')
    self.assertEqual(self.new_user.password,'Expelliarmus' )

  def test_save_user(self):
    '''
    test case to check if the user object is saved into the user list
    '''
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)
  
class TestCredentials(unittest.TestCase):
  '''
  A test case that defines test cases for credentials class
  '''

  def setUp(self):
    '''
    Method that runs before each individual credentials test method
    '''
    self.new_credential = Credentials('Hogwarts','Harry Potter','TheBoywholived')

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    Credentials.credentials_list = []
  
  def test_init(self):
    '''
    test to check if the new credentials object is initialized properly
    '''
    self.assertEqual(self.new_credential.account_name,'Hogwarts')
    self.assertEqual(self.new_credential.username,'Harry Potter')
    self.assertEqual(self.new_credential.password,'TheBoywholived')

  def test_save_credentials(self):
    '''
    test case to check if a credential object is saved into the credential_list
    '''
    self.new_credential.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)

  def test_save_multiple_credentials(self):
    '''
    Test to check if we can save mutliple credentials objects to our credentials_list
    '''
    self.new_credential.save_credentials()
    test_credentials = Credentials('Instagram','Voldemort','crUcio90')
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),2)

  def test_delete_credentials(self):
    '''
    test to see if we can remove account credentials from our credentials_list
    '''
    self.new_credential.save_credentials()
    test_credentials = Credentials('Instagram','Voldemort','crUcio90')
    test_credentials.save_credentials()

    self.new_credential.delete_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)

  def test_find_credentials_by_account_name(self):
    '''
    Test to check if we can find login credentials by account name and display information.
    '''
    self.new_credential.save_credentials()
    test_credentials = Credentials('Instagram','Voldemort','crUcio90')
    test_credentials.save_credentials()

    found_credentials = Credentials.find_credentials_by_account_name('Instagram')
    self.assertEqual(found_credentials.account_name, test_credentials.account_name)

  def test_credentials_exist(self):
    '''
    test to check if we can return a boolean if we cannot find the account credentials.
    '''
    self.new_credential.save_credentials()
    test_credentials = Credentials('Instagram','Voldemort','crUcio90')
    test_credentials.save_credentials()

    credentials_exist = Credentials.credentials_exist('Instagram')

    self.assertTrue(credentials_exist)

  def test_display_all_credentials(self):
    '''
    Test to check if all credentials in a list are being returned
    '''
    self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

  




    

if __name__ == '__main__':
    unittest.main()
