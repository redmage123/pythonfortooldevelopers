#!/usr/bin/python3

def my_generator():
    l = [1,2,3,4,5]
    for num in l:
        yield num ** 2

mg = my_generator()
while (True):
    try:
        square =  next(mg)
        print (square)
    except StopIteration:
        print ("Finished")
        break


