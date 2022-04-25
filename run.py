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

def 