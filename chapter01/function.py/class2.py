#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyClass(object):
    
    message = 'Hello, Developer.'

    def show(self):
        print self.message
        print "Here is %s in %s!" % (self.name, self.color)

    @staticmethod
    def printMessage():
        print "printMessage is called"
        print MyClass.message

    @classmethod
    def createObj(cls, name, color):
        print "Object was created: %s(%s, %s)"% (cls.__name__, name, color)
        return cls(name, color)
            
    def __init__(self, name = "unset", color = "black"):
        print "Constructor is called with params: ",name, " ", color
        self.name = name
        self.color = color
        
    def __del__(self):
        print "Destructor is called for %s!"% self.name


MyClass.printMessage()

inst = MyClass.createObj( "Toby", "Red")
print inst.message
del inst
