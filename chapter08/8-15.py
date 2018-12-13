#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_connect_string='sqlite://'

engine = create_engine(db_connect_string)
SessionType = scoped_session(sessionmaker(bind=engine,expire_on_commit=False))
def GetSession():
    return SessionType()

from contextlib import contextmanager
@contextmanager
def session_scope():
    session = GetSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()








import orm
from sqlalchemy import or_

orm.Base.metadata.create_all(engine)

def InsertAccount( user, passw, title, salary):				#新增操作
    with session_scope() as session:
        account=orm.Account(user_name=user, password=passw, title=title, salary=salary)
	session.add(account)
	return

def GetAccount(id=None, user_name=None):		#查询操作
    with session_scope() as session:
        return session.query(orm.Account).filter(or_(orm.Account.id == id, orm.Account.user_name == user_name)).first()

def DeleteAccount( user_name):				#删除操作
    with session_scope() as session:
        account = GetAccount(user_name=user_name)
	if account:	session.delete(account)

def UpdateAccount( id, user_name, password, title, salary):		#更新操作
    with session_scope() as session:
        account = session.query(orm.Account).filter(orm.Account.id==id).first()
	if not account:
            return
	account.user_name=user_name
	account.password=password
	account.salary = salary
	account.title = title


InsertAccount("David Li", "123", "System Manager", 3000)
InsertAccount("Rebeca Li", "", "Accountant", 3000)
InsertAccount("David Backer", "123", "Engineer", 3000)
InsertAccount("Siemon Bond", "xxx", "Engineer", 4000)
InsertAccount("Van Berg", "123", "General Manager", None)
InsertAccount("Howard", "123", "General Manager", 3000)

account = GetAccount(2)
print account.user_name, account.salary

DeleteAccount("Howard")
UpdateAccount(1, "admin", "none", "System Admin", 2000)



with session_scope() as session:
    for account in session.query(orm.Account):
        print account.id, account.user_name, account.title, account.salary
    




