#!/usr/bin/python2.7

import time
import cProfile

def calcsum():
    calcsum=0
    for i in range(100000):
        calcsum += i


def main() :
    calcsum()

if __name__ == "__main__":
    cProfile.run('main()')

