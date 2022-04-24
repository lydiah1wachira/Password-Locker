import unittest
from user_credentials import User

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

if __name__ == '__main__':
    unittest.main()
