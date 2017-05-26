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

engineArgs = 'mysql://' + secret_config.database_user + ":" + \
    secret_config.database_pass + "@localhost/" + secret_config.database_name + '?charset=utf8' + '?charset=utf8'
engine = create_engine(engineArgs)
Base = declarative_base()

session = sessionmaker(bind=engine)
session = session()


class Restaurant(Base):
    __tablename__ = 'Restaurant'
    id      = Column(Integer, primary_key=True)
    name    = Column(String(100))
    address = Column(TEXT)

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def rrt_save(self):
        session.add(self)
        session.commit()

    def rrt_update(self):
        session.commit()

    @staticmethod
    def rrt():
        rrt = session.query(Restaurant).first()
        print rrt
        return rrt

    def __str__(self):
        return "%s" % self.as_dict()
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
Base.metadata.create_all(engine)


