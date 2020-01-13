#!/usr/bin/python3.7

import base
import os
import cgi
import session
import authentication
import db
from http import cookies

params = cgi.FieldStorage()

if os.environ["REQUEST_METHOD"].upper() == "POST":

  user = params.getvalue("username")
  if not user:
    print("Location: change_pass_first.py")
  else:
    cookies_object = cookies.SimpleCookie()
    cookies_object["username"] = user
    print(cookies_object.output())


print("")
base.start_html()
print('''<form class="register-form" method="POST">
<h2>Change Password</h2>
Username <input type="text" name="username"/>
<input type="submit" value="Next"/>
</form>''')
base.finish_html()
