#!/usr/bin/python

import socket


class TCPClient:

    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = target_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        self.client.connect((self.target_host, self.target_port))
        self.connected = True

    def send(self, data):
        if self.connected:
            self.client.send(data)
        else:
            raise socket.error("Before Sending data you should "
                               "connect to your target first!")

    def recieve(self, len_bytes=4096):
        if self.connected:
            return self.client.recv(len_bytes)
        else:
            raise socket.error("No data can be receivied "
                               "if there is no connection!")

# USAGE_EXAMPLE


def example():
    tcp = TCPClient("www.google.com", 80)
    tcp.connect()
    try:
        tcp.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        print tcp.recieve(4096)
    except socket.error:
        print "forgot to connect! doh!"
        exit(1)

if __name__ == "__main__":
    example()
