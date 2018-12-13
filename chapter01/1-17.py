#!/usr/bin/env python
# -*- coding: utf-8 -*-

dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}

print dict1['Title']									#读取元素

dict1['Date'] = '2002-10-30'							#直接通过下标新增字典内容
print dict1

dict1['Language'] = 'Chinese'						#直接通过下标更新字典内容
print dict1

dict2 = {'Language': 'English', 'Language':'Chinese'}		
print dict2
