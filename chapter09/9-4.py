#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import DatagramProtocol
from sys import stdout

class Echo(DatagramProtocol):
    def datagramReceived(self, data):
        print data.decode('utf8')

protocol = Echo()

host = "127.0.0.1"
port = 8007

portSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
portSocket.setblocking(False)           #设为阻塞模式
portSocket.bind((host, port))

port = reactor.adoptDatagramPort(
    portSocket.fileno(), socket.AF_INET, Echo())

portSocket.close()

reactor.run()
bStop = True
