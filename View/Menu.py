import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import login_required
from Models.Menu import Menu
from Models.ErrorCode import *

mod = Blueprint('Menu', __name__, url_prefix='/menu')

@mod.route("/", methods = ['GET'])
def query_menus():
	menus = []
	for menu in Menu.menus():
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