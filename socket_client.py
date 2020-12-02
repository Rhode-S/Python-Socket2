# file: socket_client
# socket client example

#import socket library
import socket


try:
    #create an AF_INET and Stream socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #print message
    print("Congratulation, socket created!")

except socket.error:
    print("Failed to create socket", socket.error)
    exit(0)

# create host variable
host = "www.google.com"
port = 80 #default port for www

try:
    remote_ip = socket.gethostbyname(host)
    print("IP address of", host, "is", remote_ip)

    #Connect with the remote server
    s.connect((remote_ip, port))

    #message to server
    message = "GET / HTTP/1.1\r\n\r\n"

    try:
        #send the string s utf-8 encoded string
        s.send(message.encode('utf-8'))
        print("Message sent successfully")

        #receive the response in 4 byte chunks
        response = s.recv(4096)
        print(response)

    except:
        print("Failed to send the message")
        exit(0)

except:
    #could not be resolved
    print("Host couldn't be resolved, please check")
    exit(0)

s.close()