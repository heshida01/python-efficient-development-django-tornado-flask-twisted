#!/usr/bin/env python
# -*- coding: utf-8 -*-



from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Account(Base):
    __tablename__ = u'account'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    title = Column(String(50), nullable=False)
    salary = Column(Integer)

    def is_active(self):
        #"""假设所有用户都是活跃用户."""
        return True

    def get_id(self):
        #"""  返回账号ID, 用方法返回属性值提高了表的封装性."""
        return self.id

    def is_authenticated(self):
        #"""假设已经通过验证"""
        return True

    def is_anonymous(self):
        #"""具有登录名和密码的账号不是匿名用户"""
        return False






from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship, backref


class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True)
    name= Column(String(50))
    level = Column(Integer)
    address = Column(String(50))

    class_teachers = relationship("ClassTeacher", backref="class")
    students = relationship("Student", backref="class")
	
class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    name= Column(String(50))
    age = Column(Integer)
    gender= Column(String(10))
    address= Column(String(50))
    class_id = Column(Integer, ForeignKey('class.class_id'))

class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    name= Column(String(50))
    gender= Column(String(10))
    telephone= Column(String(50))
    address= Column(String(50))
    class_teachers = relationship("ClassTeacher", backref="teacher")

class ClassTeacher(Base):
    __tablename__ = 'class_teacher'
    teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'), primary_key=True)
    class_id = Column(Integer,ForeignKey('class.class_id'),primary_key=True)


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_connect_string='sqlite://'

engine = create_engine(db_connect_string)
SessionType = scoped_session(sessionmaker(bind=engine,expire_on_commit=False))
def GetSession():
    return SessionType()




Base.metadata.create_all(engine)
session = GetSession()

session.add(Class(name = u"三年二班", level = 3, address = "B3F1"))
session.add(Class(name = u"三年三班", level = 3, address = "B3F2"))
session.add(Class(name = u"一年三班", level = 1, address = "B2F1"))

session.add(Student(name = u"王晓帅", age=9, gender=u'男', address = u"浦东新区",class_id=1))
session.add(Student(name = u"林文龙", age=9, gender=u'男', address = u"黄浦区",class_id=1))
session.add(Student(name = u"李霞", age=10, gender=u'女', address = u"B3F1",class_id=1))
session.add(Student(name = u"侯梦", age=9, gender=u'女', address = u"南汇县",class_id=2))

session.add(Teacher(name = u"王天来", gender=u'男', telephone='56340688', address = u"浦东新区"))
session.add(Teacher(name = u"吴芬", gender=u'女', telephone='34129983', address = u"浦东新区"))

session.add(ClassTeacher(teacher_id = 1, class_id =1))
session.add(ClassTeacher(teacher_id = 1, class_id =2))
session.add(ClassTeacher(teacher_id = 1, class_id =3))
session.add(ClassTeacher(teacher_id = 2, class_id =1))
session.add(ClassTeacher(teacher_id = 2, class_id =2))

