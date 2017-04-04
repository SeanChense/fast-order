import sys 
sys.path.append('..') 
import secret_config

from sqlalchemy import Column, String, Integer, ForeignKey
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

	def __repr__(self):
		return "<User(%s)>" % self.name
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
session = session()

tony = User("tony", 18, 2, "jlajg89password", "http://tva1.sinaimg.cn/crop.0.0.640.640.180/005XFMkjjw8f66mx6kktij30hs0hsq3r.jpg")
session.add(tony)
session.commit()



































    

