#!/usr/bin/python3.7

import cgi, os, sys, cgitb, base
import session
import db
import webbrowser

images = ""
request_type = os.environ.get('REQUEST_METHOD', '')
if not os.path.isdir('../../htdocs/images'): 
    os.mkdir('../../htdocs/images')
 
    images = os.listdir('../../htdocs/images/')

form = cgi.FieldStorage()

data = session.get_session_data()
if data is None:
    print ("Location: login.py")
    
print ("Content-type:text/html")
print ("")
base.start_html()
if (request_type == "POST"):
    file_item = form["avatar"]
    collection = form.getvalue('collection')
    collection_id = db.save_collection(str(collection))
   

    if file_item.filename:
        fn = ('../../htdocs/images/' + str(collection) + "/")
        fn += os.path.basename(file_item.filename)
        db.save_image(file_item,collection)
        open(fn, 'wb').write(file_item.file.read(250000))
        message = 'The file "' + fn + '" was uploaded successfully'
       
    else:
        message = "No file was uploaded"

collecs = db.get_collections()

print('<form enctype="multipart/form-data" method="POST" style="margin-bottom: 100px;">')
print("<span>Collections</span>")
if(collecs):
    print('<input type="text" name="collection" list="db_colls">')
    print('<datalist id="db_colls"')
    for coll in collecs:
        print('<option>' + coll[1] + '</option>')
    print('</datalist>')
else:
    print('<input type="text" name="collection">')

print ('<input type="file"  name="avatar" accept="image/png, image/jpeg">')
print('<input type="submit" value="upload">')
print ('</form>')
print('<a class="btn" href="logout.py">Logout</a>')
print('<form method="GET">')
print("<h3> Select a collection</h3>")
print('<select name="collections">')
for coll in collecs:
    print('<option>' + coll[1] + '</option>')
print('</select>')
print('<input type="submit" value="choose">')
print("</form>")

collections = "test"
if(request_type == "GET"):
    collections = form.getvalue('collections')
    if(collections):
        images = os.listdir('../../htdocs/images/' + str(collections) +'/')

print("<br>")
print(collections)  
print("<br>")
print('<div class="imgs" style="width: max-content;">')

collection_id = db.get_collection_id_by_name(collections)[0]
db_images = db.get_images_by_collection_id(collection_id)

for image in db_images:
    print('<form action="image.py" method="POST" target="_blank" style="display: inline;">')
    print('<button type="submit">')
    print('<img src="../../images/%s" width=200 height=400>' % image[1])
    print('<input type="hidden" name="image" value="%s"/>' % image[1])
    print('<input type="hidden" name="image_id" value="%s"/>' % image[0])
    print('</button>')
    print("</form>")
print("</div>")
base.finish_html()
