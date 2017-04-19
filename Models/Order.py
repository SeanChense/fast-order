import sys 
sys.path.append('../') 
import secret_config
from Menu import *
from DinnerTable import *

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
    __tablename__ = 'od'
    id          = Column(Integer, primary_key=True, unique=True)
    amount      = Column(FLOAT)
    menus       = Column(TEXT)
    createdAt   = Column(DATETIME)
    table_id    = Column(Integer)
    uid         = Column(Integer)
    menus_obj   = []

    def __init__(self, amount, menus, table_id, uid):
        self.amount     = amount
        self.menus      = menus
        self.createdAt  = datetime.datetime.now()
        self.table_id   = table_id
        self.uid        = uid

    def order_save(self):
        print 'id %s' %self.id
        print 'uid %s' %self.uid
        session.add(self)
        session.commit()
        
        # disable table
        DinnerTable.use_table(self.table_id, self.uid)


    @staticmethod 
    def order_filter_id(id):
        order = session.query(Order).get(id)
        return Order.__query_menus(order)

    @staticmethod
    def order_filter_uid(uid):
        orders = session.query(Order).filter(Order.uid == uid).all()
        for order in orders:
            order = Order.__query_menus(order)
        return orders

    @staticmethod
    def __query_menus(order):
        if not order: 
            return None

        menus = []
        for index in order.menus.split(","):
            menus.append(Menu.menu_filter_id(index))

        order.menus_obj = menus

        return order

    @staticmethod
    def orders():
        orders = session.query(Order).all()
        return orders 

    def __str__(self):
        return "%s" % self.as_dict()

    def as_dict(self):
        desc =  {c.name: getattr(self, c.name) for c in self.__table__.columns}
        desc['createdAt'] = desc['createdAt'].strftime("%Y-%m-%d %X")
        menus = []
        for menu in self.menus_obj:
            menus.append(menu.as_dict())
        desc['menus'] = menus
        return desc

Base.metadata.create_all(engine)