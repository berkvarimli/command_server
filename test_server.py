import unittest
import socket
from socket import *
from server import threaded
from server import Main

class serverTestCase(unittest.TestCase):
    def test_threaded1(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 2113))
        client_socket.send('mkdir testtest'.encode())
        self.assertEqual(client_socket.recv(1024).decode(), 'There is no terminal output.')
        client_socket.close()
    
    def test_threaded1(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 2113))
        client_socket.send('echo test'.encode())
        self.assertEqual(client_socket.recv(1024).decode(), 'test\n')
        client_socket.close()
if __name__ == '__main__':
    unittest.main()
