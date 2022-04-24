
class User:
  '''
  Class user that generates new instances of a user
  '''
  user_list = []

  def __init__(self, username, password):
    '''
    __init__ method that helps define properties of a user object
    '''
    self.username = username
    self.password = password

  def save_user(self):
    '''
    method to save user objects into the user_list
    '''
    User.user_list.append(self) 