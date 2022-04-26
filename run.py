#!/usr/bin/env python3.8

from textwrap import shorten
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

  print("Hello Welcome to Password Locker\n")

  short_code = input('Please Enter the following short code:\n SU - create account\n SI - sign in\n').lower().strip()

  if short_code == 'su':
    print('sign up')
    print ('-'*20)
    username = input('Enter new username\n')

    while True:
      password_option = input("Choose from the following codes:\n TP- create your own password\n RP - Get a random system generated password\n").lower().strip()

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
    print('-'*40)

  elif short_code == 'si':
    print('Sign in. Enter your username and password')
    username = input(' Enter Username...\n')
    password = input('Enter Password...\n')

    signIn =  login_user(username,password)

    if login_user == signIn:
      print(f'Welcome to Password Locker, {username}\n')
      print('*' * 40)

  while True:
    short_code = input('Use the following short codes :\n CC - create new  account credentials \n  FC - Find existing credentials\n DC - Display all accounts and their credentials\n D - Delete credentials\n').lower().strip()

    if short_code == 'cc':
      print('Generate New Account Credentials')
      account = input('Account Name ...\n')
      userName = input('Enter Username ...\n')

      while True:
         password_option = input("TP- create your own password\n RP - Get a random system generated password\n").lower().strip()
         print('_'*40)
         if password_option == 'tp':
           password = input('Enter a new password\n')
           break
         elif password_option == 'rp':
           password = generate_password()
           break
         else :
           print('Invalid credentials, please try again\n')
           print('_'*40)
      save_details(create_new_credential(account, userName, password))
      print(f'Account credentials for your {account} account, username- {userName}, password - {password},  have been created succesfully\n')
    
    elif short_code == 'fc':
      search_account = input("Enter the account name you want to search for\n")
      if find_credentials(search_account):
        search_account = find_credentials(search_account)
        print(f'Account: {search_account.account}')
        print(f'Username - {search_account.username}\n password - {search_account.password}')
        print('-'*30)
      else:
        print('No credentials were found for that account\n')
        print('-'*40)

    elif short_code == 'dc':
      if display_accounts():
        print("Here is a list of all your accounts and their credentials\n")
        print('-'*30)
        for account in display_accounts():
          print(f'Account: {account.account}\n Username {username}\n password{password}')
          print('_'*30)
      else:
        print("You do not yet have any saved Credentials.\n")

    elif short_code == 'd':
      search_name = input('Enter the account you want to delete\n')
      if find_credentials(search_name):
        delete_account = find_credentials(search_name)
        delete_account.del_credentials()
        print(f'Credentials for {delete_account.account} have been successfully deleted\n')
        print('_'*40)
      else:
        print('No such credentials found\n')
        print('-'*40)
        
  
if __name__ == '__main__':
  main()


    



