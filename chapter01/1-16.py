#!/usr/bin/env python
# -*- coding: utf-8 -*-

sample2 = set([ 4, 6, -1.1, 'English', 0, 'Python'])		#初始化set

sample2.add('China')							#增加元素
print sample2

sample2.update('France')						#用序列更新
print sample2

sample2.remove(-1.1)							#删除元素
print sample2

sample3 = frozenset([ 6, 'English', 9])				#初始化frozenset

sample3.add('China')							#错误，frozenset无法更新
