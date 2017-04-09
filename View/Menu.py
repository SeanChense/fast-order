import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import login_required
from Models.Menu import Menu
from Models.ErrorCode import *

mod = Blueprint('Menu', __name__, url_prefix='/menu')

@mod.route("/", methods = ['GET'])
@login_required
def query_menus():
	menus = []
	for menu in Menu.menus():
		menus.append(menu.as_dict())
	return jsonify({"status":0, "data":menus})