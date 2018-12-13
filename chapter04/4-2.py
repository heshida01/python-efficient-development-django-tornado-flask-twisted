#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import os
if os.path.exists('sampleDB.db'):
    os.remove('sampleDB.db')


#引入peewee包的所有内容
from peewee import *

# 建立一个Sqlite数据库引擎对象，该引擎打开数据库文件sampleDB.db
db = SqliteDatabase("sampleDB.db")

# 定义一个ORM的基类，在基类中指定本ORM所使用的数据库，
# 这样在之后所有的子类中就不用重复声明数据库
class BaseModel(Model):
    class Meta:
        database = db

# 定义course表，继承自BaseModel
class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField(null = False)
    period = IntegerField()
    description = CharField()

    class Meta:
        order_by = ('title',)
	db_table = 'course'				#定义数据库中的表名

# 定义 teacher 表，继承自BaseModel
class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null = False)
    gender = BooleanField()
    address = CharField()
    course_id = ForeignKeyField(Course, to_field="id",  related_name = "course")

    class Meta:
        order_by = ('name',)
        db_table = "teacher"



#建表，仅需创建一次
Course.create_table()
Teacher.create_table()

