#!/usr/bin/python2.7
import time

calcsum = 0
start = time.time()
for i in range(10000):
    calcsum += i
finish = time.time()



print calcsum
print "%.2f" % ((finish-start) *100000)
start = time.time()
calcsum1 = sum(range(10000))
finish = time.time()
print calcsum1
print "%.2f" % ((finish-start)*100000)


