#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyClass(object):
    
    message = 'Hello, Developer.'
    
    def show(self):
        print self.message
        print "Here is %s in %s!" % (self.name, self.color)
        
    def __init__(self, name = "unset", color = "black"):
        print "Constructor is called with params: ",name, " ", color
        self.name = name
        self.color = color
        
    def __del__(self):
        print "Destructor is called for %s!"% self.name


inst2 = MyClass("David")
inst2.show()

print "Color of inst2 is ", inst2.color, "\n"

inst3 = MyClass("Lisa", "Yellow")
inst3.show()
print "Name of inst3 is ", inst3.name, "\n"

del inst2, inst3



