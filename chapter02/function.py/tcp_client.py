#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket   #socket模块

HOST='127.0.0.1'
PORT=3434

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #AF_INET说明使用

s.connect((HOST, PORT))
print "Connect %s:%d OK" % (HOST, PORT)
data = s.recv(1024)   #接收数据，本次接收数据的最大长度为1024
print "Received: ", data
s.close()                   #关闭连接
