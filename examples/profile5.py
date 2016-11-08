#!/usr/bin/python3

import time

def calcsum1():
    start=0
    finish=0
    calcsum = 0
    start = time.time()
    for i in range(10000):
        calcsum += 1
    finish = time.time()
    return finish - start

def calcsum():
    start=0
    finish=0
    start = time.time()
    calc = sum(range(10000))
    finish = time.time()
    return finish - start


def main():
    timetorun = calcsum1()
    timetorun = timetorun * 100000
    print("%.2f" % (timetorun))

    timetorun = calcsum()
    timetorun = timetorun * 100000
    print("%.2f" % (timetorun))
if __name__ == "__main__":
    main()

