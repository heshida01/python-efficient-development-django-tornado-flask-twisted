#!/usr/bin/env python
# -*- coding: utf-8 -*-

from orm2 import session, Student, Class

class_=Class()
student1, student2=Student(), Student()
class_.students.append(student1)
class_.students.append(student2)

session.add(class_)
if student1 in session:
    print "The student1 has been added too!"


