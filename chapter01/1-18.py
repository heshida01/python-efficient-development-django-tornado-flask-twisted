#!/usr/bin/env python
# -*- coding: utf-8 -*-

dict1 = {'Language': 'English', 'Title': 'Python book', 'Pages': 450}

print dict1.get('Title', 'Todo')					#读取元素

print dict1.get('Author', 'Anonymous')			#读取不存在的键

print dict1.pop('Language')							#pop

print dict1										#检查pop后的字典内容

dict2={'Author':'David', 'Price':32.00, 'Pages':409 }	
dict1.update(dict2)								#合并字典
print dict1

print dict1.values()								#获取值列表
