#!/usr/bin/python3.7

import base
import os
import cgi
import session
import authentication
import db
from http import cookies

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
username = get_all_cookies_object.get("username")

params = cgi.FieldStorage()
user = db.get_user_by_username(username)

if not username:
  print('Location: change_pass_first.py')

question_id = user[3] if user else None
question = db.get_question_by_id(question_id) if question_id else None

if os.environ["REQUEST_METHOD"].upper() == "GET":
  new_password = params.getvalue("password")
  answer = params.getvalue("answer")
  success = authentication.change_password(
            username, new_password, question_id, answer)
  if success:
    print('Location: login.py')


print("Content-type:text/html")
print("")
base.start_html()
print('''<form class="register-form" method="GET" style="color:white;">
<h2>Change Password</h2>
<p>''' + user[1] + ''' </p>
New password <input type="password" name="password"/>
<p style="display:block;">''' + question[1] + '''</p>
Answer <input type="text" name="answer"/>
<input type="submit" value="Change"/>
</form>''')
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print("<div>Change Error</div>")
base.finish_html()
