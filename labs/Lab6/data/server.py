#!/usr/bin/python3


import socket
import sys

with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    server_address = ('localhost',10080)
    sock.bind(server_address)
    sock.listen(5)

    while True:
        connection,client_address = sock.accept()

        while True:
            data = connection.recv(1024)
            if data:
                sys.stderr.write("Received %s" % data)
            else:
                break




