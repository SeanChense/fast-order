import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import login_required
from Model.Order import Order
from Model.Menu  import Menu
from Model.ErrorCode import *

mod = Blueprint('Order', __name__, url_prefix='/order')

@mod.route("/create", methods = ['POST'])
@login_required
def create_order(user):
	table_id = request.form['table_id']
	menus	 = str(request.form['menus_id'])

	if not table_id:
		return jsonify({
			"status":err_tableid_null
			})

	if not menus or len(menus.split(",")) == 0:
		return jsonify({
			"status":err_menusid_null
			})	

	amount = 0.
	for menu_id in menus.split(','):
		amount += Menu.menu_filter_id(menu_id).price
	print amount
	uid	  = user.id

	order = Order(amount, menus, table_id, uid)
	order.order_save()
	order = Order.order_filter_id(order.id)
	print order.id

	return jsonify({
		'status':0,
		'data': order.as_dict()
		})

@mod.route("/detail", methods = ['POST'])
@login_required
def order_detail(user):
	order_id = request.form['order_id']
	if not order_id:
		return jsonify({
			'status':err_orderid_null
			})

	order = Order.order_filter_id(order_id)
	print order
	if not order:
		return jsonify({
			'status':err_order_not_found
			})

	return jsonify({
		'status':0,
		'data':order.as_dict()
		})