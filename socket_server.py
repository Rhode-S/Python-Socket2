#file: socket_server.py
import socket

s = socket.socket()
host = '' # empty means all available interfaces
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Congratulation, socket created!")

try:
    s.bind((host, port))
    print("Great, socket completed")

    s.listen(10)
    print("Socket is now listening")

    #keep listening for multiple clients
    while True:
        #wait to accept a connection
        conn, addr = s.accept()
        print("Connect with", addr[0], addr[1])

        #communication with client
        data = str(conn.recv(1024))
        print(data)
        response = "OK," + data
        if not data:
            break
        conn.sendall(response.encode('utf-8'))

    #close all connections
    conn.close()
    s.close()
except socket.error:
    print("Bind failed", socket.error)
    exit(0)
