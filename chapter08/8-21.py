#!/usr/bin/env python
# -*- coding: utf-8 -*-

from orm2 import session, Student, Class

class_=Class()
student1, student2=Student(), Student()
class_.students.append(student1)
class_.students.append(student2)

session.add(class_)

class_=Class()
session.add(class_)
student3= Student()
if student3 in session:
    print "The student3 is added before append to the class_!"
    
class_.students.append(student3)
if student1 in session:
	print "The student3 is added after append to the class_!"
