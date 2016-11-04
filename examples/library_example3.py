#!/usr/bin/python3

from nettools import NetworkElement
with NetworkElement('171.0.2.45') as ne:
    for route in ne.routing_table:
        print ("%15S -> %s" % (route.name, route.ipaddr)

