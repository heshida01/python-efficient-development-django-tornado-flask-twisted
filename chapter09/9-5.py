#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import DatagramProtocol
from sys import stdout

host = "127.0.0.1"
port = 8007

class Echo(DatagramProtocol):							#定义DatagramProtocol子类
    def startProtocol(self):							#连接成功后被调用
        self.transport.connect(host, port)					#指定对方地址/端口
        print "Connection created!"
        
    def datagramReceived(self, data):					#收到数据时被调用
        print data.decode('utf8')

    def connectionRefused(self):						#每次通信失败后被调用
        print "sent failed!"

    def stopProtocol(self):
        print "Connection closed!"


protocol = Echo()

from twisted.internet import reactor
import threading, time, sys, datetime

bStop = False
def routine(factory):
while not bStop:
	   #发送数据时只需传入数据，而无需传入对方地址/端口
        protocol.transport.write("hello, I'm %s %s" % (sys.argv[1], datetime.datetime.now()))
        time.sleep(5)

threading.Thread(target=routine, args=(factory,)).start()
reactor.listenUDP(port, Echo())
reactor.run()
bStop = True
