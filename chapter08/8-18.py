#!/usr/bin/env python
# -*- coding: utf-8 -*-

from orm import session, Student, Class

for student, class_  in session.query(Student, Class).join(Class).filter(Class.level==3).all():
    print student.name, class_.name

