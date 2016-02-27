#!/usr/bin/python

import socket


class UDPClient:

    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        self.client.sendto(data, ((self.target_host, self.target_port)))

    def recieve(self, len_bytes=4096):
        """ returns a tuple of [data, addr] containing data as well as host-info
        from sending host """
        return self.client.recvfrom(4096)

# USAGE_EXAMPLE


def example():
    udp = UDPClient("ntp1.hetzner.de", 123)
    ntpq = "\x1b" + "\0" * 47  # simple ntp 'time' request
    udp.send(ntpq)
    print udp.recieve(len_bytes=1024)

if __name__ == "__main__":
    example()
