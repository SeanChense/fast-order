import sys 
sys.path.append('..') 
import secret_config

from sqlalchemy import Column, String, Integer, ForeignKey
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engineArgs = 'mysql://' + secret_config.database_user + ":" + \
	secret_config.database_pass + "@localhost/" + secret_config.database_name
engine = create_engine(engineArgs)
Base = declarative_base()

class User(Base):
	__tablename__ = 'User'
	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<User(%s)>" % self.name









Base.metadata.create_all(engine)


































    

