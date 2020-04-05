
import socket
import threading
import subprocess
import os
from _thread import *

def threaded(c):

    while True:

        data = c.recv(1024)

        if not data:
            print('Client has been disconnected.')
            break
        try:
        	if (data.decode("utf-8"))[:3] == "cd ":
        		os.chdir(os.path.abspath(data[3:]))
        		data_o = b'Directory is changed'
        	else:	
        		data_o = subprocess.check_output(data, shell=True)
        except subprocess.CalledProcessError as e:
        	c.send(b'Command is wrong\n')
        	print(e.output)

        if(len(data_o) > 0):
        	c.send(data_o)
        else:
        	c.send(b'There is no terminal output.')

    c.close()


def Main():
    host = ""

    port = 2113
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Connected to port : ", port)
    # put the socket into listening mode
    s.listen(5)
    print("Server is ready and socket is listening")


# a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
