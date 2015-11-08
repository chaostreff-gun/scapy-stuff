#!/usr/bin/env python2

"""
This script sends ICMP packets with increasing TTL to a host
to get a traceroute like output
"""

from scapy.all import *
import socket
import sys

hostname = sys.argv[1]
pkt = IP(dst=hostname) / ICMP()


def getrdns(ip):
    try:
        rdns = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return ip
    return ip + ": " + rdns


for i in range(1, 30):
    pkt.ttl = i
    reply, un = sr(pkt, retry=2, timeout=1, verbose=0)
    if len(reply) == 0:
        print i, "no reply..."
    elif reply[0][1].type == 0:
        print "Done", getrdns(reply[0][1].src)
        break
    elif reply[0][1].type == 11:
        print i, getrdns(reply[0][1].src)
    else:
        print "idontknow", reply[0][1].show()
