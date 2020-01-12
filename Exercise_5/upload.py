#!/usr/bin/python3.7

import cgi, os, sys, cgitb, base
import session
import db



request_type = os.environ.get('REQUEST_METHOD', '')
if not os.path.isdir('../../htdocs/images'): #inace ce batiti gresku svaki put kad se post-a
    os.mkdir('../../htdocs/images')
 
images = os.listdir('../../htdocs/images')

form = cgi.FieldStorage()

data = session.get_session_data()
if data is None:
    print ("Location: login.py")
    
print ("Content-type:text/html")
print ("")
base.start_html()
if (request_type == "POST"):
    #print(file_item)
    file_item = form["avatar"]
    if (file_item.filename):
        print('ime file-a ' + file_item.filename)
        print("<br>")
    else:
        print ("<div>GRESKA!!</div>")

    if file_item.filename:
        fn = '../../htdocs/images/'
        fn += os.path.basename(file_item.filename)
        

        open(fn, 'wb').write(file_item.file.read(250000))
        message = 'The file "' + fn + '" was uploaded successfully'
       
        
    else:
        message = "No file was uploaded"
collecs = db.get_collections()
print("<p>Add new collection</p>")
print('<form method="POST">')
print('<input type="text" name="collection"/>')
print('<input type="submit" value="add" />')
print("</form>")
print("<span>Collections</span>")
print('<select>')
for coll in collecs:
    print('<option val="val">' + coll.collection_name + '</option>')
print('</select>')
print('<form enctype="multipart/form-data" method="POST" style="margin-bottom: 100px;">')
print ('<input type="file"  name="avatar" accept="image/png, image/jpeg">')
print('<input type="submit" value="upload">')
print ('</form>')

print('<div class="imgs">')
for image in images:
    print('<img src="../../images/' + image +  '" width=200 height=400>')
print("</div>")
print('<a class="btn" href="logout.py">Logout</a>')
base.finish_html()
