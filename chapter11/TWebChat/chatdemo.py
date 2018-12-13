#-*- coding: UTF-8 -*-
#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

#-*- coding: UTF-8 -*-
"""Simplified chat demo for websockets.

Authentication, error handling, etc are left as an exercise for the reader :)
"""

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
import datetime

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/chatsocket", ChatSocketHandler),
        ]
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        super(Application, self).__init__(handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", messages=ChatSocketHandler.cache, clients=ChatSocketHandler.waiters, username= "游客%d" % ChatSocketHandler.client_id)

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200
    client_id = 0

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self):
        self.client_id = ChatSocketHandler.client_id
        ChatSocketHandler.client_id = ChatSocketHandler.client_id + 1
        self.username = "游客%d" % self.client_id
        ChatSocketHandler.waiters.add(self)

        chat = {
            "id": str(uuid.uuid4()),
            "type": "online",
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        ChatSocketHandler.send_updates(chat)

    def on_close(self):
        ChatSocketHandler.waiters.remove(self)
        chat = {
            "id": str(uuid.uuid4()),
            "type": "offline",
            "client_id": self.client_id,
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        ChatSocketHandler.send_updates(chat)


    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)
        parsed = tornado.escape.json_decode(message)
        self.username = parsed["username"]
        chat = {
            "id": str(uuid.uuid4()),
            "body": parsed["body"],
            "type": "message",
            "client_id": self.client_id, 
            "username": self.username,
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        chat["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=chat))

        ChatSocketHandler.update_cache(chat)
        ChatSocketHandler.send_updates(chat)


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
