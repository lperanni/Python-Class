#!/usr/bin/python3.7

import db 
import password_utils

def register(username, password):
    user_id = db.create_user(username, password.encode('utf-8'))
    if user_id:
        return True
    else:
        return False
        
def authenticate(username, password):
    user = db.get_user_by_username(username)
    if (user and password_utils.verify_password(password.encode("utf-8"), user[2].encode('utf-8'))):
        return True, user[0]
    else:
        return False, None

def change_pass(username):
    user= db.get_user_by_username(username)
    
        
    
