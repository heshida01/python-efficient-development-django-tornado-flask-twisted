#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

param = None

if len(sys.argv) > 1:
    param = int(sys.argv[1])

if param is None:
    print "Alert"
    print "The param is not set"
elif param < -10:
    print "The param is small"
elif param > 10:
    print "the param is big"
else:
    print "the param is middle"    
