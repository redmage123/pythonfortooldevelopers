#!/usr/bin/python3.5

import timeit
from ctypes import *

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return(fib(n-1) + fib(n-2))

if __name__ == "__main__":

    l = cdll.LoadLibrary("./libmymath.so")
#    for i in range(10):
#        t = timeit.Timer(lambda: fib(c_int(i).value))
#        print ('Value of n = %d\nPure python %.2f usec/pass' % (i,1000000 * t.timeit(number=100000)/100000))
#        t1 = timeit.Timer(lambda: l.fib(i))
#        print ('Value of n = %d\nCtypes python %.2f usec/pass\n' % (i,1000000 * t1.timeit(number=100000)/100000))


    div = l.divide
    div.argtypes = [c_int, c_int,POINTER(c_float)]
    x = c_int(3)
    y = c_int(10)
    remainder =c_float(0) 
    result = div(x.value,y.value,byref(remainder))
    print ("result = %d remainder = %f" % (c_int(result).value,remainder.value))
