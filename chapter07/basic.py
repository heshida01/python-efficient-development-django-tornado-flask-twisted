import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world1")

def make_app():
    return tornado.web.Application([
        (r"/index", MainHandler),
        (r"/entry/([^/]+)", EntryHandler),
    ],
    debug=True)

class EntryHandler(tornado.web.RequestHandler):
    def get(self, slug):
        self.write(slug)

def main():
    app = make_app()
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
    print "killed"

if __name__ == "__main__":
    main()
