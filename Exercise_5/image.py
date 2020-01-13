#!/usr/bin/python3.7
import cgi
import base
import db
import os
from datetime import datetime
from http import cookies


http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)

jesus = "jesus"

params = cgi.FieldStorage()
img = params.getvalue("image")
image = db.get_image_by_path(img)
image_id = params.getvalue("image_id")
cookies_object = cookies.SimpleCookie()
cookies_object["image_id"] = image_id
cookies_object["last_visited"] = datetime.now()
cookies_object["image_id"]['expires'] = 12 * 30 * 24 * 60 * 60
print(cookies_object.output())

last_time = get_all_cookies_object.get("last_visited")
#last_time_parsed = datetime.strptime(str(last_time), "%Y-%m-%d %H:%M:%S.%f")

if not get_all_cookies_object.get("image_id"):
  db.visit_image(image[0])

if os.environ["REQUEST_METHOD"].upper() == "GET" and jesus:
  img_id = params.getvalue("id_img")
  success = db.delete_image(img_id)
  if success:  
    print("Location: upload.py")
  else:
    print(img_id)

print("Content-type:text/html")
print("")
base.start_html()
print('<img src="../../images/%s" width=800 height=600>' % image[1])
print('<form method="GET">')
print('<input type="submit" value="DELETE"/>')
print('<input type="hidden" name="id_img" value="%s"/>' % image[0])
print('</form>')
base.finish_html()


