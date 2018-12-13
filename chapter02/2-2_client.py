#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket   						#socket模块

HOST='127.0.0.1'
PORT=3434

#AF_INET说明使用IPv4地址， SOCK_ DGRAM指明UDP协议
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   

data = "Hello UDP!"
s.sendto(data, (HOST, PORT))
print "Sent: %s to %s:%d" %(data, HOST, PORT)

s.close()                  				#关闭连接
