#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket   #socket模块
import datetime

HOST='0.0.0.0'
PORT=3434

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #AF_INET说明使用
s.bind((HOST,PORT))   #绑定IP与端口
s.listen(10)         #监听

while True:
       conn,addr=s.accept()   #接受TCP连接，并返回新的socket
       print'Client %s connected!' % str(addr)    #输出客户端的IP地址
       dt = datetime.datetime.now()
       message = "Current time is " + str(dt)
       conn.send(message)       #给客户端发送当前时间
       print "Sent: ", message
       conn.close()     #关闭连接
