#!/usr/bin/python3

import socket
import sys


test_sentences = [ u'Python is a wonderful language',
                  u'No lo har\x8a ma\xa4ana',
                  u'Apr\x8as vous s\x27il vous plait',
                  u'Marie \x8apouse Marie au joyeux mois de mai',
                  ]


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
    server_address = ('localhost',10080)
    sock.connect(server_address)

    for sentence in test_sentences:
        sock.send(sentence)

