#!/usr/bin/env python
# -*- coding: utf-8 -*-



from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True)
    name= Column(String(50))
    level = Column(Integer)
    address = Column(String(50))

    students = relationship("Student", backref="class_", cascade="all")
	
class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True)
    name= Column(String(50))
    age = Column(Integer)
    gender= Column(String(10))
    address= Column(String(50))
    class_id = Column(Integer, ForeignKey('class.class_id'))


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



