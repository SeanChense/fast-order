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
	secret_config.database_pass + "@localhost/" + secret_config.database_name
engine = create_engine(engineArgs)
Base = declarative_base()

class User(Base):
	__tablename__ = 'User'
	id 		= Column(Integer, primary_key=True)
	name 	= Column(String(100))
	age 	= Column(Integer)
	gender	= Column(Integer) # 0 for boy, 1 for girl, 2 for others
	password= Column(String(100))
	avatar	= Column(String(100))
	def __init__(self, name, age, gender, password, avatar):
		self.name = name
		self.age  = age
		self.gender 	= gender
		self.password 	= password
		self.avatar		= avatar

	def __str__(self):
		return "<User:id=%s, name=%s>" % (self.id, self.name)

class TTable(Base):
	__tablename__ = 'TTable'
	id 			= Column(Integer, primary_key=True)
	uid			= Column(Integer)
	available 	= Column(TINYINT)
	
	def __init__(self, uid):
		self.uid 		= uid
		self.available 	= (uid is None) # use none to free table resource

	def __str__(self):
		return "<TTable:id=%s used by uid:(%s)>" % (self.id, self.uid)		
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
session = session()




































    

