#!/usr/bin/python3
import timeit


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)


def main():
    i = 5 
    t = timeit.Timer(setup = 'from __main__ import fib', stmt = 'fib(5)')
    print ('Value of n = %.d\nPure python %.2f usec/pass' % (i,t.timeit(number=100000)))

    outputs = t.repeat(number = 1000000, repeat = 3)
    for time_value in outputs:
        print ('Value of n = %.d\nPure python %.2f usec/pass' % (i,time_value))


if __name__ == "__main__":
    main()

