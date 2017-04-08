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
	secret_config.database_pass + "@localhost/" + secret_config.database_name
engine = create_engine(engineArgs)
Base = declarative_base()

session = sessionmaker(bind=engine)
session = session()

class User(Base):
	__tablename__ = 'User'
	id 		= Column(Integer, primary_key=True)
	name 	= Column(String(100))
	age 	= Column(Integer)
	gender	= Column(Integer) # 0 for boy, 1 for girl, 2 for others
	password= Column(String(100))
	avatar	= Column(TEXT)
	token	= Column(TEXT)
	def __init__(self, name, password, age=None, gender=None, avatar=None):
		self.name = name
		self.age  = age
		self.gender 	= gender
		self.password 	= password
		self.avatar		= avatar

	def generate_auth_token(self, expiration = 600):
		s = Serializer(secret_config.SECRET_KEY, expires_in = expiration)
		self.token = s.dumps({ 'id': self.id })
		session.commit()
		return self.token


	def user_save(self):
		session.add(self)
		session.commit()

	@staticmethod
	def user_filter_name_password(name, password):
		user = session.query(User).filter(User.name == name, User.password == password).first()
		return user

	@staticmethod 
	def user_filter_id(id):
		user = session.query(User).filter(User.id == id).first()
		return user

	@staticmethod
	def verify_auth_token(token):
		s = Serializer(secret_config.SECRET_KEY)
		try:
		    data = s.loads(token)
		except SignatureExpired:
		    return None # valid token, but expired
		except BadSignature:
		    return None # invalid token
		user = User.user_filter_id(data['id'])
		return user

	def __str__(self):
		return "<User:id=%s, name=%s>" % (self.id, self.name)
	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class TTable(Base):
	__tablename__ = 'TTable'
	id 			= Column(Integer, primary_key=True)
	uid			= Column(Integer)
	available 	= Column(TINYINT)
	
	def __init__(self, uid):
		self.uid 		= uid
		self.available 	= (uid is None) # use none to free table resource

	def __str__(self):
		if self.available:
			return "<TTable:id=%s available>" % (self.id)		
		else:
			return "<TTable:id=%s used by uid:(%s)>" % (self.id, self.uid)		
Base.metadata.create_all(engine)

