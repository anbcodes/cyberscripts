#
# Connect over TCP to the following server 'localhost', 10000
# Initiate communication with GET to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#


import time
import socket
import math
import re

HOST = 'localhost'  # The server's hostname or IP address
PORT = 10000        # The port used by the server

def utf(s):
  return bytes(s, 'utf-8')

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shift(s, a):
  newStrArr = []
  for group in s.split(' '):
    newStrGroup = []
    for char in group:
      newStrGroup.append(alpha[(alpha.find(char) + i) % len(alpha)])
    newStrArr.append(''.join(newStrGroup))
  return ' '.join(newStrArr)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(utf('GET'))
    data = s.recv(1024)
    print('Received', repr(data))
    datas = data.decode('utf-8').split('\n')[1:]
    print('datas', repr(datas))
    found = []
    for s2 in datas:
      for i in range(1, 26):
        t = shift(s2, i)
        if re.match(r'^[a-zA-Z0-9 ]*$', t) and (
          t.find(' ME ') != -1 or
          t.find(' ALL ') != -1 or
          t.find(' ALADDIN ') != -1 or
          t.find(' HE ') != -1 or
          t.find(' HER ') != -1 or
          t.find(' AND ') != -1 or
          t.find(' IS ') != -1 or
          t.find(' TO ') != -1 or
          t.find(' IN ') != -1 or
          t.find(' ONE ') != -1 or
          t.find(' HIM ') != -1 or
          t.find(' WHEN ') != -1 or
          t.find(' PROVIDE ') != -1 or
          t.find(' EAT ') != -1 or
          t.find(' FOR ') != -1 or
          t.find(' VERY  ') != -1 or
          t.find(' THE ') != -1 ):
        	found.append(t)
    print('found', found)
    if len(found) == 3:
      s.sendall(bytes('\n'.join(found), 'utf-8'))
      data = s.recv(1024)
      print('Received final', repr(data))
