#!/usr/bin/python3
import timeit

def wrapper(func, *args,**kwargs):
    def wrapped():
        return func(*args,**kwargs)
    return wrapped


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)


def main():
    i = 5 
    wrapped = wrapper(fib,i)
    t = timeit.Timer(wrapped,number=10000)
    print ('Value of n = %d\nPure python %.2f usec/pass' % (i,t.timeit()))



if __name__ == "__main__":
    main()

