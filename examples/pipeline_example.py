#!/usr/bin/python3

import time

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0,1)
            continue
        yield line

def mygrep(pattern,lines):

    for line in lines:
        if pattern in line:
            yield line



with open('/var/log/syslog') as lf:
    getloglines = follow(lf)
    getpatternlines = mygrep('python',getloglines)
    
    for line in getpatternlines:
        print (line)
    
