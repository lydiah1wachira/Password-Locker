class Credentials():
  '''
  class that generates new instances of account names and their credentials.
  '''
  def __init__(self, account_name, username, password):
    '''
    __init__ method that helps us define properties for our objects

    Args:
        account_name: new user social account name
        username: new user username 
        password: new user password
    '''
    self.account_name = account_name
    self.username = username
    self.password = password


