#!/usr/bin/python3.7

import base
import os,cgi
import session
import authentication

params = cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    username = params.getvalue("username")
    password = params.getvalue("password")
    success, user_id = authentication.authenticate(username, password)
    if success:
        session_id = session.create_session()
        session.add_to_session({"user_id": user_id}, session_id=session_id)
        print ('Location: upload.py')


print("Content-type:text/html")
print("")
base.start_html()
print ('''<form class="register-form" method="POST">
<h2>LOGIN</h2>
username <input type="text" name="username" />
password <input type="password" name="password"/>
<input type="submit" value="Login"/>
</form>''')
print('<a class="btn" href="register.py">Register</a>')
print('<a class = "btn" href = "change_pass_first.py" > Change Password </a>')
if (os.environ["REQUEST_METHOD"].upper() == "POST" and not success):
    print ("<div>Login Error</div>")
base.finish_html()
