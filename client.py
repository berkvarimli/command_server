
import socket
import os

def Main():
    host = '127.0.0.1'
    port = 2113

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    message = input("Enter Command : ")
    while True:
     
        s.send(message.encode('ascii'))

        data = s.recv(1024)

        print('Received from the server :', str(data.decode('ascii')))
        
        ans = input('\nEnter a new command or press (n) :') 
        if ans == 'n':
            
            break
        else: 
            message = ans
            continue
        
    # close the connection
    s.close()


if __name__ == '__main__':
    Main()
