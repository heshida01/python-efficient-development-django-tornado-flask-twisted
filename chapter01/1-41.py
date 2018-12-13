#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseA(object):
    def move(self):
        print "move called in BaseA!"

class BaseB(object):
    def move(self):
        print "move called in BaseB!"

class BaseC(BaseA):
    def move(self):
        print "move called in BaseC!"

class Sub(BaseC, BaseB):
    pass
    
inst = Sub()
inst.move()
