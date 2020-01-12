#!/usr/bin/python3.7

import base
import os
import cgi
import session
import authentication
import db

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username = params.getvalue("username")
    password = params.getvalue("password")
    success = db.change_user_password(username, password.encode('utf-8'))
    if success:
      print('Location: login.py')

print("")
base.start_html()
print('''<form class="register-form" method="POST">
<h2>Change Password</h2>
Username <input type="text" name="username" />
New password <input type="password" name="password"/>
<input type="submit" value="Change"/>
</form>''')
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print("<div>Login Error</div>")
base.finish_html()
