#!/usr/bin/env python3.8

from users import User
from credentials import Credentials

def create_new_user(username,password):
  '''
  Function to create a new  password-Locker user with a username and password
  '''
  new_user = User(username,password)
  return new_user

def save_user(user):
  '''
  Function to save a user
  '''
  user.save_user()

def login_user(username,password):
  '''
  Function that verifies whether a user exists and then logs them in 
  '''
  confirm_user = Credentials.verify_user(username,password)
  return confirm_user

def create_new_credential(account, username, password):
  '''
  function that creates new credentials for a specific user account
  '''
  new_credentials = Credentials(account,username,password)
  return new_credentials

def save_details(credentials):
  '''
  Function to save credentials to the credentials list
  '''
  credentials.save_credentials()

def del_credentials(credentials):
  '''
  Function to delete credentials from the credentials list
  '''
  credentials.delete_credentials()

def display_accounts():
  '''
  Function that returns all saved credentials
  '''
  return Credentials.display_credentials()

def find_credentials(account):
  '''
  Function that finds an account's credentials from the account name
  '''
  return Credentials.find_credentials_by_account_name(account)

def check_credentials(account):
  '''
  Function to check if credentials exist for a specific account.
  '''
  return Credentials.credentials_exist(account)

def generate_password():
  '''
  Function that generates a random password for a user 
  '''
  rando_password = Credentials.generate_random_password()
  return rando_password

def main():

  print("Hello Welcome to Password Locker\n Please Enter the following short code:\n SU - create account\n SI - sign in \n")

  short_code = input('Please Enter the following short code:\n SU - create account SI - sign in').lower().strip()

  if short_code == 'su':
    print('sign up')
    print ('-'*20)
    username = input('Enter new username\n')

    while True:
      password_option = input("Choose from the following codes:\n TP- create your own password\n RP - Get a random system generated password").lower().strip()

      if password_option == 'tp':
        password = input('Enter new Password...\n')
        break 
      elif password_option == 'rp':
        password = generate_password()
        break
      else:
        print("Invalid password please try again")
    save_user(create_new_user(username,password))

    print('-'*40)
    print(f'Hello {username}, your Password Locker account has been successfully created and your password is {password}')

  elif short_code == 'si':
    print('Sign in. Enter your username and password')
    username = input(' Enter Username...\n')
    password = input('Enter Password...\n')

    signIn =  login_user(username,password)
    


