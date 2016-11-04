#!/usr/bin/python3

# Put the import statements on separate lines for readability
# Also, it's nice to alphabetize them if you have a lot
# of imports. 
import jnettool.tools.elements.NetworkElement
import jnettool.tools.Routing
import jnettool.tools.RouteInspector

ne = jnettool.tools.elements.NetworkElement('171.0.2.45')

try:
    routing_table = ne.getRoutingTable()
except jnettool.tools.elements.MissingVar:
    logging.exception('No routing table found')
    ne.cleanup('rollback')
else:
    num_routes-routing_table.getSize()
    for RToffset in range(num_routes) :
        route = routing_table.getRouteByIndex(RToffset)
        name = route.getName()
        ipaddr = route.getIPAddr()
        print ("%15s -> %s" % *name, ipaddr)
finally:
    ns.cleanup('commit')
    ns.disconnect()
