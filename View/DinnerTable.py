import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import login_required
from Models.DinnerTable import DinnerTable
from Models.ErrorCode import *

mod = Blueprint('DinnerTable', __name__, url_prefix='/table')

@mod.route("/", methods = ['GET'])
@login_required
def query_tables():
	tables = []
	for table in DinnerTable.tables():
		tables.append(table.as_dict())
	return jsonify({"status":0, "data":tables})