#!/usr/bin/env python
# -*- coding: utf-8 -*-

tuple1 = ('you', 456, 'English', 9.34)				#定义

print tuple1[2]								#读取元素

print tuple1[1:]								#截取子元组

tuple1[2]='France'							#错误！不能修改元组内容

tuple2 = (3, 'you and me')					
tuple1 = tuple1 + tuple2						#可以对元组变量重新赋值

print tuple1

print len(tuple2)								#用函数len()获得元组长度
