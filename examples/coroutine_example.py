#!/usr/bin/python3
import math


def exponent(s):
    while True:
        p = yield
        print (math.pow(s,p))

def generator(start):

    start +=1
    yield start

e = exponent(2)
e.send(None)

e.send(generator(1))
e.send()

