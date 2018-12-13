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

#新增行
Course.create(id = 1, title = '经济学', period = 320, description = '文理科学生均可选修')
Course.create(id = 2, title = '大学英语', period = 300, description = '大一学生必修课')
Course.create(id = 3, title = '哲学', period = 100, description = '必修课')
Course.create(id = 104, title = '编译原理', period = 100, description = '计算机系选修')
Teacher.create(name= '白阵君', gender = True, address = '..', course_id = 1)
Teacher.create(name= '李森', gender = True, address = '..', course_id = 3)
Teacher.create(name= '张雯雯', gender = False, address = '..', course_id = 2)

#查询一行
record = Course.get(Course.title=='大学英语')
print "课程：%s, 学时：%d" % (record.title, record.period)

#更新
record.period = 200
record.save()

#删除
record.delete_instance()

#查询所有记录
courses = Course.select()
for i in courses:
    print i.id, i.title, i.period, i.description

#带条件查询，并将结果按period字段倒序排序
courses = Course.select().where(Course.id< 10).order_by(Course.period.desc())
for i in courses:
    print i.id, i.title, i.period, i.description

#统计所有课程的平均学时
total = Course.select(fn.Avg (Course.period).alias('avg_period'))
for i in total:
    print u"平均学时：", i.avg_period
    
#更新多个记录
Course.update(period = 300).where(Course.id > 100).execute()

#多表连接操作，Peewee会自动根据ForeignKeyField的外键定义进行连接：
Record = Course.select().join(Teacher).where(Teacher.gender==True)
for i in Record:
    print i.id, i.title, i.period, i.description
