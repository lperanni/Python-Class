#!/usr/bin/python3.7

import base
import cgi, os
import authentication

params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == "POST":
    username = params.getvalue("username")
    password = params.getvalue("password")
    repeat = params.getvalue("repeat_password")
    question = params.getvalue("question")
    answer = params.getvalue("answer")
    if password == repeat :
        success = authentication.register(username, password, question, answer)
        if success:
            print('Location: login.py')
print()
base.start_html()
print ('''<form class="register-form" method="POST">
<h2>REGISTER</h2>
username <input type="text" name="username" />
password <input type="password" name="password"/>
Repeat password <input type="password" name="repeat_password"/>
Security Question <input type="text" name="question" />
Answer <input type="text" name="answer"/>
<input type="submit" value="Register"/>
</form>''')
print('<a class="btn" href="login.py">Login</a>')
if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Registration Error</div>")
base.finish_html()
