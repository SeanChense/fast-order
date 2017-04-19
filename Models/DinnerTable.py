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
    secret_config.database_pass + "@localhost/" + secret_config.database_name
engine = create_engine(engineArgs)
Base = declarative_base()

session = sessionmaker(bind=engine)
session = session()
class DinnerTable(Base):
    __tablename__ = 'DinnerTable'
    id          = Column(Integer, primary_key=True)
    uid         = Column(Integer)
    available   = Column(TINYINT)
    
    def __init__(self, uid):
        self.uid        = uid
        self.available  = (uid is None) # use none to free table resource

    def __str__(self):
        if self.available:
            return "<DinnerTable:id=%s available>" % (self.id)       
        else:
            return "<DinnerTable:id=%s used by uid:(%s)>" % (self.id, self.uid) 
            
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def tables():
        tables = session.query(DinnerTable).all()
        return tables     

    @staticmethod
    def table_filter_id(id):
        table = session.query(DinnerTable).get(id)
        return table

    @staticmethod
    def use_table(id, uid):
        table = DinnerTable.table_filter_id(id)
        if not table:
            print "table %s not found" % (id)
            return -1

        table.uid = uid
        table.available = 0
        session.commit()

        return 0

    @staticmethod
    def free_table(id):
        table = DinnerTable.table_filter_id(id)
        if not table:
            print "table %s not found" % (id)
            return -1

        table.uid = None
        table.available = 1
        session.commit()

        return 0


Base.metadata.create_all(engine)