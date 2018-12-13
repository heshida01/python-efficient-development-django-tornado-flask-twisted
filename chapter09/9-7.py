#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import reactor, defer

def makeDefer(x):
    d = defer.Deferred()
    reactor.callLater(2, d.callback, x)
    return d

def print square(failure):
    print d*d

d = getDummyData(3)
d.addCallback(printData)

reactor.run()               #挂起运行，两秒后执行
