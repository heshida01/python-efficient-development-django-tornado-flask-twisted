#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyClass(object):
    
    message = 'Hello, Developer.'
    
    def show(self):
        print self.message
        
    def __init__(self, name = "unset", color = "black"):
        print "Constructor is called with params: ",name, " ", color
        
inst = MyClass()
inst.show()

inst2 = MyClass("David")
inst2.show()

inst3 = MyClass("Lisa", "Yellow")
inst3.show()

inst4 = MyClass(color = "Green")
inst4.show()

