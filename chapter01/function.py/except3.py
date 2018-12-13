#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
class MyError(Exception):
    def __str__(self):
        return "I'm a self-defined Error!"

def main():
    try:
        print "**********Start of main()************"
        if len(sys.argv)==1:
            raise MyError()
        print "**********End of main()************"
    except MyError, e:
        print e

if __name__ == '__main__':
    main()
