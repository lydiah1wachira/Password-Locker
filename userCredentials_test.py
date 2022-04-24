import unittest
from users import User

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

if __name__ == '__main__':
    unittest.main()
