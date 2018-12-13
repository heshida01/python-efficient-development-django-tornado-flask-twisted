#!/usr/bin/env python
# -*- coding: utf-8 -*-

myList = ['you', 456, 'English', 9.34]				#定义

print myList[2]								#读取元素

print myList[1:]								#截取子列表

myList[2]='France'							#可以修改内容
print myList

print len(myList)								#用函数len()获得列表长度

numList = [2, 8, 16, 1, -6, 52, -1]					#定义
print sorted(myList)							#排序

print myList								#sorted后myList本身并不改变

print sum(numList)							#求和
