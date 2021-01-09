import time
import socket
import math

HOST = 'localhost'  # The server's hostname or IP address
PORT = 10000        # The port used by the server

def en(s):
    return bytes(s, 'utf-8')
def de(s):
    return s.decode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    s.sendall(en('testMessage'))

    print('Received', repr(data))

