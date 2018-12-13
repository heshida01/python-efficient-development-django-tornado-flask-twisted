#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)

clients = dict()									# 客户端Session字典

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index.html")

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):							#有新链接是被调用
        self.id = self.get_argument("Id")
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}		#保存Session到clients字典

    def on_message(self, message):        			#收到消息时被调用
        print "Client %s received a message : %s" % (self.id, message)
        
    def on_close(self):							#关闭连接时被调用
        if self.id in clients:
            del clients[self.id]
            print "Client %s is closed" % (self.id)

    def check_origin(self, origin):
        return True

app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/websocket', MyWebSocketHandler),
])

import threading
import time

#启动单独的线程运行此函数，每隔1秒钟向所有的客户端推送当前时间
def sendTime():								
    import datetime
    while True:
        for key in clients.keys():
            msg = str(datetime.datetime.now())
            clients[key]["object"].write_message(msg)
            print "write to client %s: %s" % (key,msg)
        time.sleep(1)

  
if __name__ == '__main__':
    threading.Thread(target=sendTime).start()			#启动推送时间线程
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()			#挂起运行
