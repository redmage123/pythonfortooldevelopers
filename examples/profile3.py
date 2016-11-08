#!/usr/bin/python3

import time

def calcsum():
    start = time.time()
    calc = sum(range(10000))
    finish = time.time()
    return finish-start


timetorun = calcsum()

print("%.2f" % (timetorun)* 100000)

