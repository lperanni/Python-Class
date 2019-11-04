import socket
import re
import requests


host = 'www.watchthatpage.com'
links = [host]
currentIndex = 0


'''
def connect_to_host():
  global host
  PORT = 80
  host_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host_connection.connect((host, PORT))
  return host_connection

def send_request(client):
  global host
  request = "GET / HTTP/1.1\r\nHost:%s/\r\n\r\n" % host
  client.send(request.encode())
  response = client.recv(2000)  
  return response

'''

def send_request_with_requests_lib(link):
  response = requests.get('http://' + link)
  return response

def print_info(body):
  global links
  print(body) 
  print("\n\n")
  print(links)
  print("Links list size: " + str(len(links)))

def check_if_link_visited(toCheck):
  global host
  if(links.count(str(host + '/' + toCheck)) > 0):
    return True

  return False

def check_if_full_link(link):
  if(link.startswith('http')):
    return True
  else:
    return False

  

def crawl(index):
  global links
  global host
  linksToCheck = []
  print("Currently visited: " + links[index])
  body = send_request_with_requests_lib(links[index])
  if(body.status_code != 200):
    return 
    
  try:
    linksToCheck = re.findall('a href=[\'"]?([^\'" >]+)', body.content.decode())
  except:
    print("Link is bad")
    return

  for link in linksToCheck:
    if(check_if_link_visited(link) == False):
      if(check_if_full_link(link)):
        links.append(link)
      else:
        links.append(host + '/' + link)
  print_info(body)


# Main Body

for i in range(50):
  crawl(i)
  






 # client = connect_to_host()
# http_response = send_request(client).decode()

# links = re.findall(r'a href=[\'"]?([^\'" >]+)', http_response)

# print(http_response)

