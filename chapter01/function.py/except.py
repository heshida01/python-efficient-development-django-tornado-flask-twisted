#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    print 3/0
    print "This is never been called"
except:
    print "Exception happened"
finally:
    print "Process finished!"
