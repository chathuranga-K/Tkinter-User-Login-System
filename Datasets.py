"""
This file contains all the User login information & Passwords
"""

def save_info(login_username,login_password):
    userinfo = {
        login_username: {
            'username' : login_username,
            'password' : login_password
        }
    }