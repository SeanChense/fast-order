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

import datetime

engineArgs = 'mysql://' + secret_config.database_user + ":" + \
    secret_config.database_pass + "@localhost/" + secret_config.database_name
engine = create_engine(engineArgs)
Base = declarative_base()

session = sessionmaker(bind=engine)
session = session()


class Order(Base):
    __tablename__ = 'Order'
    id          = Column(Integer, primary_key=True)
    sum_price   = Column(FLOAT)
    menu_count  = Column(Integer)
    menus       = Column(TEXT)
    createdAt   = Column(DATETIME)
    table_id    = Column(Integer)
    uid         = Column(Integer)

    def __init__(self, sum_price, menu_count, menus, table_id, uid):
        self.sum_price  = sum_price
        self.menu_count = menu_count
        self.menus      = menus
        self.createdAt  = datetime.datetime.now()
        self.table_id   = table_id
        self.uid        = uid

    def order_save(self):
        session.add(self)
        session.commit()

    @staticmethod 
    def order_filter_id(id):
        order = session.query(Order).get(id)
        return menu

    @staticmethod
    def order_filter_uid(uid):
        orders = session.query(Order).filter(Order.uid == uid).all()
        return orders

    @staticmethod
    def menus():
        menus = session.query(Order).all()
        return orders 

    def __str__(self):
        return "%s" % self.as_dict()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
Base.metadata.create_all(engine)