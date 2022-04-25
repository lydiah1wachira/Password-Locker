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