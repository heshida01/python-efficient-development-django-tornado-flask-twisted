#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import Protocol

clients = []

class Spreader(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            (u"欢迎来到Spread Site, 您是第%d个客户端用户！\n" %
            (self.factory.numProtocols,)).encode('utf8'))
        print "new connect: %d" % self.factory.numProtocols
        clients.append(self)

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1
        clients.remove(self)
        print "lost connect: %d" % self.factory.numProtocols

def dataReceived(self, data):
    if data == "close":
        self.transport.loseConnection()
        for client in clients:
            if client != self:
                client.transport.write(data)



from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class SpreadFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return Spreader(self)

# 8007是本服务器的监听端口，建议选择大于1024的端口
endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(SpreadFactory())
reactor.run()									#挂起运行
