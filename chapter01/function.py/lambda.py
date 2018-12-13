#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def namedFunc(a):
    return  "I'm named function with param %s"% a
    
    
def call_func(func, param) :
    print datetime.datetime.now()
    print func(param)
    print ""
    
if __name__ == '__main__':
    call_func(namedFunc, 'hello')
    call_func(lambda x: x*2, 9)
    call_func(lambda x: x*x, -4)
