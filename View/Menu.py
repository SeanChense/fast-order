#!/usr/bin/python
#coding:utf-8
import sys 
sys.path.append('/home/ubuntu/work/fast-order') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import *
from Models.Menu import Menu
from Models.ErrorCode import *
import json

mod = Blueprint('Menu', __name__, url_prefix='/menu')

menucategory = [
"今日推荐",\
"盖浇饭",\
"面食",\
"炒饭",\
"汤饭"
]

@mod.route("/", methods = ['GET'])
def query_menus():
	menus = []
	for menu in Menu.menus():
		menu.category = menucategory[menu.category_id]
		menus.append(menu.as_dict())
	return jsonify({"status":0, "data":menus})

@mod.route("/detail", methods = ['POST'])
def menus_detail():
	menu_id = request.form['menu_id']
	if not menu_id:
		return jsonify({
			'status': err_menu_id_null
			})

	menu = Menu.menu_filter_id(menu_id)

	if not menu:
		return jsonify({
			'status':err_menu_not_found
			})

	return jsonify({
		'status':0,
		'data':menu.as_dict()
		})

@mod.route("/delete", methods = ['POST'])
@superadmin_required
def delete_menu(admin):
	menu_ids = request.form['menu_ids']
	menu_ids = json.loads(menu_ids)
	if not menu_ids:
		return jsonify({
			"status": ErrorCode.err_menusid_null
			})
	Menu.delete_menu_by_ids(menu_ids)

	return jsonify({
		"status":0
		})


@mod.route("/update", methods = ['POST'])
@superadmin_required
def update_menu(admin):
	menu_id = request.form['menu_id']
	newDict = json.loads(request.form['dict'])
	
	if not menu_id:
		return jsonify({
			"status":ErrorCode.err_menuid_null
			})

	if not newDict:
		return jsonify({
			"status":ErrorCode.err_menu_update_payload_null
			})

	Menu.update_menu_by_id(menu_id, newDict)

	return jsonify({
		"status":0
		})

@mod.route("/add", methods = ['POST'])
def add_menu():
	menu_array = json.loads(request.form['menu'])
	Menu.insert_menu(menu_array)

	return jsonify({
		"status":0
		})















