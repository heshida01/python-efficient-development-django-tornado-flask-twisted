#!/usr/bin/env python
# -*- coding: utf-8 -*-

myList = [ 4, 6, -1.1, 'English', 0, 'Python']			
sample2 = set(myList)							#初始化set
sample3 = frozenset([ 6, 'English', 9])				#初始化frozenset

print 6 in sample2							#判断包含关系

print  sample2 >= sample3						#判断子集关系

print  sample2 - sample3						#差运算

print sample2 & sample3						#交运算

sample3 |= sample2							#可以对frozenset执行 |= 重新赋值
print sample3
