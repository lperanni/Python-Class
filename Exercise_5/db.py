#!/usr/bin/python3.7

import mysql.connector  

import json
import password_utils
from datetime import datetime

db_conf = {
    "host":"localhost",
    "db_name": "authentication_project",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def destroy_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()

def create_user(username, password):
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    hashed_password = password_utils.hash_password(password)
    values = (username, hashed_password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid 

def get_user_by_username(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
    myresult = cursor.fetchone()
    return myresult

def get_user(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id='" + str(user_id) + "'")
    myresult = cursor.fetchone()
    return myresult

def get_users():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    return myresult

def change_user_password(username, password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    hashed_password = password_utils.hash_password(password)
    values = (username, hashed_password)
    query = 'UPDATE users SET password = %s WHERE username = %s'
    cursor.execute(query, values)
    mydb.commit()


def delete_user(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM users WHERE user_id='" + str(user_id) + "'")
    mydb.commit()

def save_image(file, collection_name ,collection_id ):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = ("INSERT into image (path, counter, created, last, collection_id) VALUES (%s, %d, %s, %s, %s))")
    values = ("images/" + collection_name + "/" + file.filename, 0, datetime.now(), datetime.now(), collection_id)
    cursor.execute(query, values)
    mydb.commit()

def get_collections():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("Select collection_name from collections")
    myresult = cursor.fetchall()
    return myresult

