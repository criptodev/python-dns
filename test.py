#!/usr/bin/python

import socket

### configure me ###

dns_server_ip = '1.1.1.1'
dns_server_port = 53
query = 'google.com' # change this to the hostname you want to lookup

### configure me ####

size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((dns_server_ip,dns_server_port))
s.send(('domain:' + query).encode('utf-8'))
data = s.recv(size)
s.close()
print (data)