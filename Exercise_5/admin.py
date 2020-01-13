#!/usr/bin/python3.7
import db
import base
import session


images = db.get_all_images()

data = session.get_session_data()
if data is None:
  print("Location: login.py")

user = db.get_user(data['user_id'])

if  user[4] != 2:
  print("Location: upload.py")


print("Content-type:text/html")
print("")
base.start_html()
for image in images:
  print('<img src="../../images/%s" width=100 height=100>' % image[1])
  print('<p>%s : viewed %d times</p>' % (image[1], image[2]))
base.finish_html()
