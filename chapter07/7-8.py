#!/usr/bin/env python
# -*- coding: utf-8 -*-



import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def main():
    app = make_app()
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()			#启动IOLoop
    except KeyboardInterrupt:
        print "cdddd"
        tornado.ioloop.IOLoop.current().stop()			#停止IOLoop
	
    print "Program exit!"							#此处执行资源回收等工作			


if __name__ == "__main__":
    main()
