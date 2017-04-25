#!/usr/bin/python
#coding:utf-8
import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Models.Restaurant import Restaurant
from Models.ErrorCode import *

mod = Blueprint('Restaurant', __name__, url_prefix='/restaurant')

@mod.route("/", methods = ['GET'])
def main():
	return jsonify({
		'status':0,
		'data':Restaurant.rrt().as_dict()
		})

@mod.route('/', methods = ['POST'])
# @admin_required
def modify():
	name = request.form['name'].encode('utf-8')
	address = request.form['address'].encode('utf-8')
	
	if not name:
		return jsonify({
			'status': err_restaurant_name_null
			})

	rrt = Restaurant.rrt()
	rrt.name = name

	if address:
		rrt.address = address

	rrt.rrt_update()

	return jsonify({
		"status":0
		})