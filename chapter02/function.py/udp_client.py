#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket   #socket模块

HOST='127.0.0.1'
PORT=3434

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #AF_INET说明使用
data = "Hello UDP!"
s.sendto(data, (HOST, PORT))
print "Sent: %s to %s:%d" %(data, HOST, PORT)
s.close()
                   #关闭连接
