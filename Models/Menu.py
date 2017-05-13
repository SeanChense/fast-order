import sys 
sys.path.append('/home/ubuntu/work/fast-order') 
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


class Menu(Base):
    __tablename__ = 'Menu'
    id      = Column(Integer, primary_key=True)
    name    = Column(String(100))
    category= Column(TEXT)
    category_id = Column(Integer)
    price	= Column(FLOAT)
    image   = Column(TEXT)
  

    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def menu_save(self):
        session.add(self)
        session.commit()

    @staticmethod 
    def menu_filter_id(id):
        menu = session.query(Menu).get(id)
        return menu

    @staticmethod
    def delete_menu_by_ids(ids):
        for _id in ids:
            print "goint to delete menu " + str(_id)
            session.query(Menu).filter_by(id=_id).delete()

        session.commit()

    @staticmethod
    def update_menu_by_id(id, payload):
        menu = Menu.menu_filter_id(id)
        if not menu:
            return
        for (key, value) in payload.iteritems():
            setattr(menu, key, value)
        session.commit()

    @staticmethod
    def insert_menu(payloads):
        for payload in payloads:
            menu = Menu()
            for (key, value) in payload.iteritems():
                setattr(menu, key, value)
            session.add(menu)
        session.commit()


    @staticmethod
    def menus():
        menus = session.query(Menu).all()
        return menus 

    def __str__(self):
        return "%s" % self.as_dict()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
Base.metadata.create_all(engine)




