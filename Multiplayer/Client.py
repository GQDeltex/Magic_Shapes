import socket

class Client():
   def __init__(self,Adress=("127.0.0.1",5000)):
      self.s = socket.socket()
      self.s.connect(Adress)

TC=Client()
