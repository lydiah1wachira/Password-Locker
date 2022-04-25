class Credentials:
  '''
  Class credential that generates new instances of credentials
  '''
  credentials_list = []

  def __init__(self, account_name,username,password):
    '''
    method that helps define properties of a credentials object
    '''
    self.account_name = account_name
    self.username = username
    self.password = password
  
  def save_credentials(self):
    '''
    Method that saves a credential object into a credential list
    '''
    Credentials.credentials_list.append(self)

  def delete_credentials(self):
    '''
    Method to delete saved account credentials from the credentials_lsit
    '''
    Credentials.credentials_list.remove(self)


