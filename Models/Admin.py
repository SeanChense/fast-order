#!/usr/bin/python
#coding:utf-8
import sys 
sys.path.append('..') 
import secret_config

from sqlalchemy import Column, String, Integer, ForeignKey
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

engineArgs = 'mysql://' + secret_config.database_user + ":" + \
    secret_config.database_pass + "@localhost/" + secret_config.database_name + '?charset=utf8'
engine = create_engine(engineArgs)
Base = declarative_base()

session = sessionmaker(bind=engine)
session = session()


class Admin(Base):
    __tablename__ = 'Admin'
    id      = Column(Integer, primary_key=True)
    name    = Column(String(100))
    age     = Column(Integer)
    gender  = Column(Integer) # 0 for boy, 1 for girl, 2 for others
    password= Column(String(100))
    avatar  = Column(TEXT)
    token   = Column(TEXT)
    title   = Column(String(100))
#   1       superadmin/boss
#   2       waiter/waitress
#   3       cook
    permission = Column(Integer)
    def __init__(self, name, password, permission, age=None, gender=None, avatar=None):
        self.name = name
        self.age  = age
        self.gender     = gender
        self.password   = password
        self.avatar     = avatar
        self.permission = permission

        if permission == 1:
            self.title = '超级管理员'
        if permission == 2:
            self.title = '服务员'
        if permission == 3:
            self.title = '后厨'

    def generate_auth_token(self, expiration = 6000000):
        s = Serializer(secret_config.SECRET_KEY, expires_in = expiration)
        self.token = s.dumps({ 'id': self.id })
        session.commit()
        return self.token

    @staticmethod
    def admin_filter_name_password(name, password):
        admin = session.query(Admin).filter(Admin.name == name, Admin.password == password).first()
        return admin

    @staticmethod 
    def admin_filter_id(id):
        admin = session.query(Admin).get(id)
        return admin

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return -1 # valid token, but expired
        except BadSignature:
            return -2 # invalid token
        admin = Admin.admin_filter_id(data['id'])
        return admin

    @staticmethod
    def get_staff_all():
        staff = session.query(Admin).all()

        return staff

    @staticmethod
    def update_admin_by_id(id, payload):
        admin = Admin.admin_filter_id(id)
        if not admin:
            return
        for (key, value) in payload.iteritems():
            setattr(admin, key, value)
        session.commit()

    def __str__(self):
        return "%s" % self.as_dict()
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
Base.metadata.create_all(engine)