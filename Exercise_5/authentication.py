#!/usr/bin/python3.7

import db 
import password_utils
import session

def register(username, password, question, answer):
    question_id = db.create_question(question, answer)
    user_id = db.create_user(username, password.encode('utf-8'), question_id)
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

def change_password(username, new_password, question_id, answer):
    question = db.get_question_by_id(question_id)
    correct = question[2]
    success = db.change_user_password(username, new_password.encode('utf-8'))
    if success:
        return True
    else:
        return False

   
    
        
    
