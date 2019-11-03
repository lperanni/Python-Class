import socket
import _thread

currentMessage = ""


def start_server():

  IP = '127.0.0.1'
  PORT = 42300
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((IP, PORT))
  s.listen()
  return s

def connect_to_node_4():
  recipient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  recipient.connect(('127.0.0.1', 42400))
  return recipient

def send_message(recipient):
  global currentMessage
  while True:
    currentMessage = input("Enter Message: ")
    recipient.sendall(str.encode(currentMessage))

def pipeline(prev, following):
  global currentMessage

  while True:
    message_to_send = prev.recv(1024).decode()
    if (message_to_send == currentMessage): 
      print("Arrived at destination") 
    else: 
      print(message_to_send)
      following.sendall(str.encode(message_to_send))


server = start_server()
print("Awaiting Permission to connect to next node ... ")
input()
following = connect_to_node_4()


_thread.start_new_thread(send_message, (following, ))

while True:
  prev, adress = server.accept()
  pipeline(prev, following)

