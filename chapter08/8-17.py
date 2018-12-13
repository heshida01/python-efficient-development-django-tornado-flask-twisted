#!/usr/bin/env python
# -*- coding: utf-8 -*-

from orm import session, Student, Class

sStudents = session.query(Student).join(Class).filter(Class.level==3).all()
for student in sStudents:
    print student.name



