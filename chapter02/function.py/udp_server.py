#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket   #socket模块

HOST='0.0.0.0'
PORT=3434

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #AF_INET说明使用
s.bind((HOST,PORT))   #绑定IP与端口

while True:
    data, addr = s.recvfrom(1024)
    print "Received: %s from %s" % (data, str(addr))

s.close()
