import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import login_required
from Models.Order import Order
from Models.Menu  import Menu
from Models.ErrorCode import *

mod = Blueprint('Order', __name__, url_prefix='/order')

@mod.route("/create", methods = ['POST'])
@login_required
def create_order(user):
	table_id = request.form['table_id']
	menus	 = str(request.form['menus_id'])

	amount = 0.
	for menu_id in menus.split(','):
		amount += Menu.menu_filter_id(menu_id).price
	print amount
	uid	  = user.id

	order = Order(amount, menus, table_id, uid)
	Order.order_save(order)
	order = Order.order_filter_id(order.id)[0]
	return jsonify({
		'status':0,
		'data':order.as_dict()
		})