#!/usr/bin/env python3
""" New user operations - Routines for user to interact with the API. """
from app.api.v1.database_model import DatabaseManager

class SignUp(DatabaseManager):
    """ Holds method to register new users """
    def __init__(self, user_reg_info):
        # 
        pass

    def check_username_already_exist(self):
        # Truthy
        pass
    
    def check_email_already_exist(self):
        # Truthy
        pass

    def gen_passwd_hash(self):
        """ generates hashed password """
        pass

    def register_user(self):
        """ Register user - Save user info to Database """
        # Stringify all fields b4 save???
        pass


