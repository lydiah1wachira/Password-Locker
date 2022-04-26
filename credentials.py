from users import User
import random
import string

class Credentials:
  '''
  Class credential that generates new instances of credentials
  '''
  credentials_list = []

  @classmethod
  def verify_user(cls,username,password):
    '''
    method to verify whether user is in the user_list
    '''
    current_user = ""
    for user in User.user_list:
      if(user.username == username and user.password == password):
        current_user == user.username
    return current_user

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

  @classmethod
  def find_credentials_by_account_name(cls, account):
    '''
    Method that takes in an account_name and returns credentials that match that account name 

    Args:
        account_name: the account name to search for eg twitter.
    
    Returns:
          Login credentials associated with that account.
    '''
    for credential in cls.credentials_list:
      if credential.account_name == account:
        return credential

  @classmethod
  def credentials_exist(cls, account):
    '''
    Method to check if credentials for a specific account exist by using the account name.

    Args:
        account_name : account name to search if it's credentials exist
    
    Returns:
        Boolean: True or False depending if the account exists.
    '''
    for credential in cls.credentials_list:
      if credential.account_name == account:
        return True

  @classmethod
  def display_credentials(cls):
    '''
    Method to display a list of all credentials.
    '''
    return cls.credentials_list


  def generate_random_password(passLength = 9):
    '''
    Method to generate a random password string containing letters, number and special characters
    '''
    random_password = string.ascii_letters + string.digits + "!@#$%^&*"
    random.shuffle(random_password)

    new_password = " "
    for i in range(passLength):
      new_password.append(random.choice(random_password))
    return "".join(new_password)














