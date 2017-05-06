import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import *
from Models.DinnerTable import DinnerTable
from Models.ErrorCode import *

mod = Blueprint('DinnerTable', __name__, url_prefix='/table')

@mod.route("/", methods = ['GET'])
@waiter_required
def query_tables(admin):
	tables = []
	for table in DinnerTable.tables():
		tables.append(table.as_dict())
	return jsonify({"status":0, "data":tables})



@mod.route('/free/', methods = ['POST'])
@waiter_required
def free_table(admin):
	table_id = request.form['table_id']
	if not table_id:
		return jsonify({
			'status':err_tableid_null
			})

	ret = DinnerTable.free_table(table_id)

	if ret == -1:
		return jsonify({
			'status':err_table_not_found
			})

	return jsonify({
		'status':0
		})
