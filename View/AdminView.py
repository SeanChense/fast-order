import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from flask import render_template
from Decorator import *
from Models.Admin import Admin
from Models.ErrorCode import *

mod = Blueprint('Admin', __name__, url_prefix='/admin')

@mod.route("/")
def main():
	return "Welcome to admin!"

@mod.route("/login", methods = ["POST"])
def login():
	username = request.form['username']
	password = request.form['password']

	admin = Admin.admin_filter_name_password(username, password)
	print admin
	if admin is None:
		resp = { "status":err_password_wrong
		}
		return jsonify(resp)
	else:
		admin.generate_auth_token()
		data = admin.as_dict()
		del data["password"]

		resp = { "status":0,
		"data" : data
		}
		out = jsonify(resp)
		out.set_cookie('authed', admin.token)

		return out	



@mod.route('/menu.html', methods = ['GET'])
@superadmin_required
def menu(admin):
	return render_template('menu.html')

@mod.route('/table.html', methods = ['GET'])
@superadmin_required
def table(admin):
	return render_template('table.html')