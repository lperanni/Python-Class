#!/usr/bin/python3.7

import bcrypt

salt = bcrypt.gensalt()

def hash_password(password):
    
    hashed = bcrypt.hashpw(password, salt) 
    return hashed

def verify_password (password, hash):
 
    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False

