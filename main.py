import socket

port = 53
ip = '127.0.0.1'

# Change "socket.SOCK_DGRAM" for "socket.SOCK_STREAM" for use TCP instead of UDP  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Accept only one paramether, thats why the double parenthesis
sock.bind((ip, port))

while 1:
    data, addr = sock.recvfrom(512)
    print(data)