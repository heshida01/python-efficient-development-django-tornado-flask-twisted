#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Base(object):
    def __init__(self ):
        print "Constructor of Base is called !"
        
    def __del__(self):
        print "Destructor of Base is called !"

    def move(self):
        print "move called in Base!"

class SubA(Base):
    def __init__(self ):
        print "Constructor of SubA is called !"
        
    def move(self):
        print "move called in SubA!"

class SubB(Base):
    def __del__(self):
        print "Destructor of SubB is called !"
        super(SubB, self).__del__()
        
    
instA = SubA()
instA.move()
del instA
print "--------------------------"
instB = SubB()
instB.move()
del instB
