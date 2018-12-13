#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum(x, y, z ):
    return x + y + z
    
if __name__ == '__main__':
    #如下两种调用方式的意义相同
    ret1 = sum(1, 2, 3)
    ret2 = sum( y = 2, z = 3, x = 1)

    print 'return of sum( 1, 2, 3):', ret1
    print 'return of sum( y = 2, z = 3, x = 1):', ret2
