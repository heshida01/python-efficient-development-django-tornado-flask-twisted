#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyClass(object):

    message = 'Hello, Developer.'

    def show(self):
        print self.message

    def __init__(self):
            print "Constructor is called"

inst = MyClass()
inst.show()

